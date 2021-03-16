var isl = [
    { 'team': 'mumbicity', 'mp': 15, 'won': 10, 'drawn': 3, 'loss': 2, 'gf': 22, 'ga': 8, 'gd': 14, 'points': 33 },
    { 'team': 'goa', 'mp': 16, 'won': 5, 'drawn': 8, 'loss': 3, 'gf': 24, 'ga': 19, 'gd': 5, 'points': 3 },
    { 'team': 'hyderabad', 'mp': 16, 'won': 5, 'drawn': 8, 'loss': 3, 'gf': 20, 'ga': 16, 'gd': 4, 'points': 23 },
    { 'team': 'bengluru', 'mp': 16, 'won': 4, 'drawn': 7, 'loss': 5, 'gf': 19, 'ga': 19, 'gd': 0, 'points': 19 },
    { 'team': 'kerala blasters', 'mp': 16, 'won': 3, 'drawn': 6, 'loss': 7, 'gf': 20, 'ga': 27, 'gd': -7, 'points': 15 }
]

// find all team name

// isl.map(object=>object.team).forEach(team=>console.log(team))

// // sort the team based on matches played(mp)

// isl.sort((ob1,ob2)=>ob1.mp>ob2.mp?-1:1).forEach(ob=>console.log(ob))

// find highest point form the list and print details of that player

const max_pt=isl.map(ob=>ob.pts).reduce((pt1,pt2)=>pt1>pt2?pt1:pt2)
console.log(max_pt);