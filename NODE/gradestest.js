var book = require("./grades").book;
//setUp will run before every test
exports["setUp"] =function(callback){
    book.reset();
    callback();
};

exports["Can add new grade"] = function(test){
    book.addGrade(90);
    var count = book.getCountOfGrades();
    test.equal(count,1);
    test.done();
};

exports ["check letter grades A"] = function(test){
    book.addGrade(100);
    book.addGrade(90);
    var lettergrade = book.getLetterGrade();
    test.equal (lettergrade,"A");
    test.done();
};
exports["Can average grades"] = function(test){
    book.addGrade(100);
    book.addGrade(50);
    var average = book.getAverage();
    test.equal(average,75);
    test.done();
};