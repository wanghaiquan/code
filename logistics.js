/**
 * 本地物流最后2km实现思路
 */

module.exports = Logistics;

/**
 * 三方物流信息入库操作，这个操作必须有仓管录入，然后打出自由面板，自由物流配送
 * 属性如下
 */

function Logistics() {
  this.stauts = 0; //物流状态

  /**
   * 模拟api数据
   * 第三方物流信息，这个是通过API得到的，具体可以通过生成单号去查询，这个可以去看下
   * 快递100，接口是开放的 https://www.kuaidi100.com 申请就可以了
   */
  this.info = {
    'goods': {
      'goods_id':100,
      status:'灵丘总仓揽收',
      'name':'联想（Lenovo） 小新M7268W 黑白激光无线办公家用打印机WiFi多功能一体机(打印 复印 扫描）',
      'information': [{
          'id': 1,
          'time': '2019-07-18 03:52:40',
          'desc': '【东莞市】 快件离开 【虎门中心】 已发往【太原中转】'
        },
        {
          'id': 2,
          'time': '2019-07-18 03:50:13',
          'desc': '【东莞市】 快件已经到达 【虎门中心】'
        },
        {
          'id': 3,
          'time': '2019-07-18 01:01:48	 ',
          'desc': '【深圳市】 快件离开 【福田华强南】 已发往 【大同中转部】'
        },
        {
          'id': 4,
          'time': '2019-07-18 00:34:50',
          'desc': '【深圳市】 【福田华强南】（0755-82271106、0755-82052095） 的 时冲冲客户（13641483731） 已揽收'
        }
      ]
    }
  }
}


/**
 * 入库操作 ，生成本地配送面板
 * @operator int  录入员
 * @goods   array 商品信息
 */
Logistics.prototype.entry = function( operator , goods ) {
  return 'this';
}

/**
 * 获取三方物流信息， 通过kuaidi100 API得到物流信息
 */
Logistics.prototype.get = function() {
   return this.info.goods;
}

/**
 * 加入本地物流信息
 */
Logistics.prototype.add = function( id , status, desc , time  ) {
  this.info.goods.status = status
  this.info.goods.information.push(
    {
      'id': id,
      'time': time,
      'desc': desc
    }
  )
}
/**
 * 根据商品ID查询物流信息
 */
Logistics.prototype.search = function(goods_id) {

}

var G = new Logistics()

// 手机APP一个， 可以用微信条形码 ， 可更改数据状态

/**
* 01 仓管入库，并生成面单 ,继承原始信息
* G.entry ('张三',goods)
*/

/**
* C端查看物流信息
* G.get()
*/


//获取三方物流信息
//console.log(G.get())

//总仓配送 1
G.add(5,'灵丘总仓正在配送中....' , '【灵丘县】【总仓】XXX配送中， 15234210291','2019-07-18 08:34:50' )

G.add(6,'东河南揽收' , '【灵丘县】【东河南】XXX配送中， 15234210292','2019-07-18 08:40:50' )

G.add(7,'以收入' , '' ,'2019-07-18 08:40:50')

console.log( G.get () )
