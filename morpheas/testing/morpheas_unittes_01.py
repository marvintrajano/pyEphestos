import unittest
import bpy
from math import sqrt

print("\n---------- test-- Morphas-----------\n\n")
#PKHG checking objects
def check_contains(cl,name , print_value = False, no_underscore = True):
    dir_class = dir(cl)
    for el in dir_class:
        if el.startswith("_") and no_underscore:
            pass
        else:
            if print_value:
                tmp = getattr(cl,el)
                print(name , " contains ==>",el," value = ", tmp)
            else:
                print(name , " contains ==>",el)
    print("\ncheck_contains finished\n\n")

Ephestos = None
morph = None

class morphas_1_Test(unittest.TestCase):

    def setUp(self):
        global Ephestos, morph
###### imp.reload seems not to work locals() strang 6-4-2012
#        print("\n-------setUp called locals() =", locals())
        if True: #"bpy" in locals():
#            print("L29 bpy in locals")
            import imp
            import Ephestos
            imp.reload(Ephestos.morpheas)
            morph = Ephestos.morpheas
        else:
            import Ephestos
            print(dir(Ephestos))
            from Ephestos import morpheas as morph
#        check_contains(Ephestos,"ephestos")# , print_value = True, no_underscore = True)

    def test_load_Ephestos(self):
#PKHG.OK        print("------ test_morphas_1")
        import Ephestos

#        print(dir(Ephestos))
#PKHG.OK        print("--------- type Ephestos", type(Ephestos))
# type Ephestos <class 'module'>
        self.assertTrue(Ephestos)

    def test_morphas_point_1(self):
        global Ephestos
        from Ephestos import morpheas as morph
        assertTrue = self.assertTrue
        assertEqual = self.assertEqual
        assertFalse = self.assertFalse

#        check_contains(Ephestos.morpheas,"morphas" , print_value = True, no_underscore = True)
#PKHG.OK        check_contains(morph,"morphas") # , print_value = True, no_underscore = True)
        P1 = morph.Point(10,10)
        P2 = morph.Point(20,10)
        assertTrue(P1)
        assertEqual(P1.__repr__(),  '10@10', msg = "should be '10@10'") #check for __init__ and __repr__
        assertTrue(P1 != P2)#, msg = "should different") 
        assertFalse(P1 < P2)
        assertTrue(P1 <= P2)
        assertFalse(P2 > P1)
        assertTrue(P2 >= P2)
        assertTrue(P2 >= P1)
        assertTrue(P2 >= P2)
        P3 = morph.Point(10.1,10.5)  #rounding goes to EVEN choice!#        print(round(P3))
        assertTrue(round(P3) == P1) #ok because of 'even' choice ...
        assertTrue(P1.max(P2) == P2)
        assertTrue(P1.min(P2) == P1)
        assertTrue( P1 + P2 == morph.Point(30,20))
        assertTrue(P1 + 4 == morph.Point(14,14))
        assertTrue(P2 - P1 == morph.Point(10,0))
        assertTrue(P2 - 10 == morph.Point(10,0))
        assertTrue(P2 * P2 == morph.Point(400,100))
        assertTrue(P2 * 4 == morph.Point(80,40))
        assertTrue(P2 / P1 == morph.Point(2,1))
#PKHG= 1@0.5        print(P2 / 20)
        assertTrue(P2 / 20 == morph.Point(1,0.5))
        assertTrue(P2 // morph.Point(3,3) == morph.Point(6,3))
        assertTrue(P2 // 20 == morph.Point(1,0))
        assertTrue(abs(-P2) == P2)
        assertTrue( P1.dot_product(P2) == 300)
        assertTrue( P2.cross_product(P1) == 100)
        assertTrue( P1.distance_to(P2) == sqrt(100))
        assertTrue( P1.rotate('pi',P2) == morph.Point(30,10)) #        print("======",P1.rotate('pi',P2))
#        print("======",P1.rotate('right',P2))
        assertTrue( P1.rotate('right',P2) == morph.Point(20,10)) #
#        print("======",P1.rotate('left',P2))
        assertTrue( P1.rotate('left',P2) == morph.Point(20,10)) #
        P4 = morph.Point(3,7)
#        print("----------------",P1.rotate('pi',P4))
        assertTrue( P1.rotate('pi',P4) == morph.Point(-4,4)) 
#        print("======",P1.rotate('pi',P2))
#        print("======",P1.rotate('right',P4))
        assertTrue( P1.rotate('right',P4) == morph.Point(0,10)) 
        assertTrue( P1.rotate('left',P4) == morph.Point(6,4)) 
        assertTrue( P2.scale_by(P1) == morph.Point(200,100))
        assertTrue( P2.translate_by(P1) == P1 + P2)
        assertTrue( P2.scale_by(P1) == P1 * P2)
        assertTrue( P2.as_list() == [20, 10])
        #P3 = morph.Point(10.1,10.5)
        #P2 = morph.Point(20,10)

        F1 = P3.flip('vertical',P2)
#PKHG, File "*\Ephestos\morpheas.py", line 117, in flip
        assertEqual(F1.x, P3.x)
        assertEqual(F1.y, 2*P2.y - P3.y)
        assertEqual(F1, morph.Point(10.1,9.5))

        #P3 = morph.Point(10.1,10.5)
        #P2 = morph.Point(20,10)
        F2 = P3.flip('horizontal',P2)
        assertEqual(F2.y, P3.y)
        assertEqual(F2.x, 2*P2.x - P3.x)
        assertEqual(F2, morph.Point(29.9, 10.5))             

        #P4 = morph.Point(3,7)
        P5 = morph.Point(4,6)
        R1 = P4.rectangle(P5)
        assertEqual( R1 , P5.rectangle(P4))
        assertEqual( R1.origin, morph.Point(3,6))
        assertEqual( R1.corner, morph.Point(4,7))
        #P3 = morph.Point(10.1,10.5)
        R2 = P3.extent(P5)
        self.assertNotEqual(R1,R2) #for these examples!
        assertEqual( R2.origin, P3 )
        assertEqual( R2.corner, P3 + P5)

    def test_rectangle(self):
        global Ephestos, morph
#PKHG.OK        check_contains(morph,'morph')
        assertEqual = self.assertEqual

        origin = morph.Point(20,20)
        corner = morph.Point(30,50)
        R1 = morph.Rectangle(origin,corner)
        assertEqual(R1.origin, origin)
        assertEqual(R1.corner, corner)
        assertEqual(str(R1),'(20@20 | 30@50)')
        assertEqual(R1.area(), (30 - 20) * (50 - 20))
        R2 = morph.Rectangle(origin,-corner)
        assertEqual(R2.area(),0)        
        assertEqual(R1.bottom(), 20)
        center = R1.center()
        top_left = R1.origin
        bottom_right = R1.corner
        assertEqual(R1.top_left(), morph.Point(20,50))
        center = (top_left + bottom_right) // 2
#PKHG.OK        print("center = ", center) #= 25@35
        assertEqual(R1.bottom_center(), morph.Point(25,20))
        assertEqual(R1.bottom_left(), morph.Point(20,20))
        assertEqual(R1.bottom_right(), morph.Point(30,20))
        assertEqual(R1.bounding_box(), R1)           
        assertEqual(R1.center(), center)
        corners = R1.corners()
        assertEqual(len(corners), 4)
#PKHG.OK all 4 are Point:        print([type(el) for el in corners])

        assertEqual(R1.extent(), morph.Point(30 - 20, 50 - 20))
        assertEqual(R1.height(), 50 - 20)
        assertEqual(R1.left(), 20)
        assertEqual(R1.left_center(), morph.Point(20,35))
        assertEqual(R1.right(), 30)
        assertEqual(R1.right_center(),morph.Point(30,35))
        assertEqual(R1.top(), 20)
        assertEqual(R1.top_center(), morph.Point(25, 50))
        assertEqual(R1.top_left(), morph.Point(20, 50))
        assertEqual(R1.top_right(), morph.Point(30, 50))
        self.assertTrue( R1 == R1)
        self.assertTrue( R1 != R2)

#Rectangle functions
        delta = 5
        R3 = R1.inset_by(delta)
#PKHG,= (25@25 | 25@45)         print(R3)
        self.assertTrue(type(R3) == type(R1))
        leftPoint = origin + delta
        rightPoint = corner - delta
        assertEqual( R3, morph.Rectangle(leftPoint,rightPoint))
        Rtest = morph.Rectangle(morph.Point(1,5),morph.Point(4,4))
#PKHG.= (1@5 | 4@4)        print(Rtest)
        R4 = R1.inset_by(Rtest)
#PKHG.=(21@25 | 26@46)        print(R4)

        R5 = R1.expand_by(4.5)
#PKHG.=(15.5@15.5 | 34.5@54.5)        print(R5)
        tmp =  R1.origin - morph.Point(4.5,4.5)
        assertEqual(R5.origin, tmp)

        R6 = R5.intersect(R1)
#PKHG.= (20@20 | 30@50)        print(R6)
        R7 = R1.intersect(R5)
#PKHG.=(20@20 | 30@50)        print(R7)

#PKHG.TODO merge rest of Rectangle 6-4-2012
        R8 = R1.merge(R5)
#PKHG.=(20@20 | 30@50) (15.5@15.5 | 34.5@54.5) (15.5@15.5 | 34.5@54.5)
#        print(R1,R5,R8)
        self.assertTrue(R1.contains_point(morph.Point(25,40)))
        self.assertFalse(R1.contains_point(morph.Point(25,50)))
        self.assertTrue(R8.contains_rectangle(R1))
        self.assertTrue(R8.contains_rectangle(R5))
        self.assertTrue(R8.intersects(R1))
        P_0 = morph.Point(0,0)
        P_1 = morph.Point(1,1)
        self.assertFalse(R8.intersects(morph.Rectangle(P_0,P_1)))
        assertEqual(R8.scale_by(P_1),R8)
        assertEqual(R8.scale_by(P_0),morph.Rectangle(P_0,P_0))
        assertEqual(R8.translate_by(P_0),R8)
        assertEqual(R8.translate_by(0),R8)
#PKHG R8 = (15.5@15.5 | 34.5@54.5)
        assertEqual(R8.translate_by(morph.Point(2,4)),
                    morph.Rectangle(morph.Point(17.5,19.5),
                                    morph.Point(36.5,58.5)))
    def test_Node(self):        
        assertTrue = self.assertTrue
        assertEqual = self.assertEqual
        assertFalse = self.assertFalse
        n1 = morph.Node(name = 'PKHG')
        assertTrue(n1 != None)
        assertEqual(n1.name, 'PKHG')
        assertEqual( str(n1), 'aNode(PKHG)')
        n2 = morph.Node()
        n1.add_child(n2)
        assertEqual(n2.depth(),1)
        assertEqual(n1.root(),n1)
        assertEqual(n2.root(),n1)
        allChildren = n1.all_children()
        assertEqual(allChildren,[n1,n2])
        n1.remove_child(n2)
        assertEqual(n1.root(),n1)
        assertFalse(n2.root() == n1)
        assertFalse(n2.depth() == 1)
        n3 = morph.Node(name="n3")
        n1.add_child(n2)
        n2.add_child(n3)
        allLeafs = n1.all_leafs()
        assertEqual(allLeafs,[n3])
        allParents = n3.all_parents()
        assertEqual(allParents,[n3,n2,n1])
        n4 = morph.Node(name="n4")
        n1.add_child(n4)
        n4Siblings = n4.siblings()
        assertEqual(n4Siblings , [n2])
        myMorph = morph.Morph()
        n4.add_child(myMorph)
        parents = myMorph.all_parents()
#PKHG.inform myself ;-)        print("all_parents test")
#PKHG.=        print([(el,"is of type",type(el)) for el in parents])
#[(Morph, 'is of type', <class 'Ephestos.morpheas.Morph'>), (aNode(n4), 'is of type', <class 'Ephestos.morpheas.Node'>), (aNode(PKHG), 'is of type', <class 'Ephestos.morpheas.Node'>)]
#PKHG.NOTE strange a result of 'super' ???!
        '''
        tmp = myMorph.parent_of_class(type(n1))
        tmp2 = type(n1)
        tmp3 = type(myMorph)
        print(dir(myMorph))
        print("\n=====",tmp,tmp2,tmp3)
        assertEqual(myMorph.parent_of_class(type(n1)),n4)        
        assertEqual(n1.child_of_class(type(myMorph)),myMorph)
        '''

    def test_Morph_init(self):
        assertTrue = self.assertTrue
        assertEqual = self.assertEqual
#PKHG.Error        Minit = morph.Morph(name="mymorph")
#TypeError: __init__() got an unexpected keyword argument 'name'
        Minit = morph.Morph()
        Minit.name ="mymorph"
#PKHG.= 'node'        print(Minit.name)
        assertEqual(Minit.name, "mymorph")
        assertEqual(Minit.color, (0.3, 0.3, 0.3, 1.0))
        assertTrue(Minit.is_visible)
        assertTrue(Minit.is_draggable)
        assertEqual(Minit.fps, 0)

    def test_Morph_other(self):
        assertTrue = self.assertTrue
        assertEqual = self.assertEqual
        assertFalse = self.assertFalse

        M0 = morph.Morph()
        assertEqual(M0.name, "node")
        assertEqual(M0.delete(),None)

        M0 = morph.Morph()
#PKHG.= <class 'Ephestos.morpheas.Rectangle'>        print(type(M0.bounds))
        assertEqual(M0.bounds.area(), 6000)
        assertEqual(M0.delete(), None)
        M0 = morph.Morph()
        M1 = morph.Morph()
        M0.add_child(M1)
        assertEqual(M1.depth(),1)
        M2 = morph.Morph()
        M1.add_child(M2)
        Rect = morph.Rectangle(morph.Point(-3,-5),morph.Point(0,60))
        M1.bounds = Rect
        assertEqual(M2.depth(),2)
        assertTrue(M0.wants_to_step())
        M1.is_visible = False
        assertFalse(M1.wants_to_step())
#PKHG.= [0@0, 0@40, 50@40, 50@0]        print(M0.corners())
#PKHG.= (-3@-5 | 50@60)        print(M0.full_bounds())

    def test_Hand_init(self):
        assertTrue = self.assertTrue
        assertEqual = self.assertEqual
        assertFalse = self.assertFalse
        H1 = morph.Hand()
        assertTrue(H1)
        assertFalse(H1.world)
        assertEqual(H1.mouse_over_list,[])
        assertEqual(H1.bounds, morph.Rectangle(morph.Point(0,0),morph.Point(0,0)))

    def test_Hand_functions(self):
        assertTrue = self.assertTrue
        assertEqual = self.assertEqual
        assertFalse = self.assertFalse
        H1 = morph.Hand()
        H1.world = morph.World()
#        check_contains(H1,'H1',print_value= True)
#PKHG:  H1 contains children
#PKHG,= []        print(H1.world.broken)
        assertEqual(H1.world.broken, [])
        assertEqual(H1.children , [])
        H1.world.add(morph.Morph())
        H1.world.add(H1)
        H1.changed()     
#PKHG.= [Morph, Hand(0@0)]        print(H1.world.children)
#PKHG.= []        print(H1.world.broken)

    def test_World_from_init(self):
        assertTrue = self.assertTrue
        assertEqual = self.assertEqual
        assertFalse = self.assertFalse

        mW = morph.World() 
        mW_bounds = mW.bounds
#PKHG.= a long list ;-)        check_contains(mW,"World")
#PKHG.= (0@0 | 800@600)        print(mW.bounds)


#PKHG.INFO the next checks  are in fact checking Rectangle again
        PZW = mW_bounds.bottom_left()
        assertEqual(PZW , morph.Point(0,0))
        PW = mW_bounds.left_center()
        assertEqual(PW, morph.Point(0, 300))
        PNW = mW_bounds.top_left()
        assertEqual(PNW, morph.Point(0, 600))
        PN = mW_bounds.top_center()
        assertEqual(PN, morph.Point(400, 600))
        PNE = mW_bounds.top_right()
        assertEqual(PNE, morph.Point(800, 600))
        PE = mW_bounds.right_center()
        assertEqual(PE, morph.Point(800, 300))
        PZE = mW_bounds.bottom_right()
        assertEqual(PZE, morph.Point(800, 0))        
        PZ = mW_bounds.bottom_center()
        assertEqual(PZ, morph.Point(400, 0))        


        

########activate the test
if __name__ == '__main__':
    suite =     unittest.TestLoader().loadTestsFromTestCase(morphas_1_Test)
#    unittest.TextTestRunner(verbosity=3).run(suite)
    unittest.TextTestRunner(verbosity=1).run(suite) #one gives points for OK tests
    
