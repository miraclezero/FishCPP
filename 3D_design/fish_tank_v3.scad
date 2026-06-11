$fn=50;
difference() {translate([0,0,0])cube([220+12+6, 87.5+10, 116.5+6+8+20], center=true);
 
    translate([0,-46,3+18])cube([220+5+6, 3, 116.5+8], center=true);
    translate([0,0,-50+10])cube ([220+5+8,87.5+10,4], center=true);

    translate([0,0,3]) cube ([220+6,87.5+11,116.5+8+20.1], center=true);
    translate([110,0,72])rotate([0,90,0]) cylinder(r=1.5, h=10);//inlet hole
    translate([-120,0,72])rotate([0,90,0]) cylinder(r=1.5, h=10);//inlet hole

}
difference(){translate([0,47.25,3+18-5])cube([220+14
, 3, 116.5], center=true);
    #translate([0,0,-50+10])cube ([230+5+6,84+11,3.5], center=true);
}
difference(){translate([0,0,-55])cube ([10,87.5+10,30], center=true);
    translate([0,0,-50+10])cube ([230+5+6,87.5+18,3.5], center=true);
}
translate([90,0,-73]) cube ([3,92+20,3], center=true);
translate([-90,0,-73]) cube ([3,92+20,3], center=true);
translate([30,0,-73]) cube ([3,92+20,3], center=true);
translate([-30,0,-73]) cube ([3,92+20,3], center=true);

//translate([0,-46,3+18])cube([220+6, 1, 117], center=true); //front cover board

//
//translate([0,0,0])cube([90, 2, 113], center=true);
//translate([0,2,58.])cube([105, 6, 3], center=true);
//#translate([51,2,56.])cube([4, 6, 7], center=true);
//#translate([-51,2,56.])cube([4, 6, 7], center=true); //division