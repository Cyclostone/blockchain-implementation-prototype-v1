class Lion {
  constructor(name, hairColor) {
    this.name = name;
    this.hairColor = hairColor;
  }

  logName() {
    console.log("Roar!!!!! I am ", this.name);
  }
}

const goldenLion = new Lion("Mufasa", "golden");
console.log(goldenLion);
goldenLion.logName();

const redLion = new Lion("Shanks", "red");
console.log(redLion);
redLion.logName();

const runloop = (param_1, param_2) => {
  for (let i = 0; i < 10; i++) {
    console.log(i);
    if (i === 5) {
      console.log("Yes it is 5 only");
    }
  }
  console.log(param_1);

  param_2();
};

const logBam = () => {
  console.log("yohohohohoho");
};

runloop("kakashi", logBam);
