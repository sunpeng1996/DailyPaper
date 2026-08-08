---
title: 'EvReflection: Event-Driven Micro-Dynamics for Reflection Removal'
title_zh: EvReflection：基于事件驱动微动力学的图像反射去除方法
authors:
- Jiaxiao Wang
- Dachun Kai
- Huyue Zhu
- Quanquan Hu
- Zhenyang Xu
- Xiaoyan Sun
affiliations:
- University of Science and Technology of China
- Institute of Artificial Intelligence, Hefei Comprehensive National Science Center
arxiv_id: '2608.06184'
url: https://arxiv.org/abs/2608.06184
pdf_url: https://arxiv.org/pdf/2608.06184
published: '2026-08-06'
collected: '2026-08-08'
category: Other
direction: 事件相机 · 图像反射去除优化
tags:
- Event Camera
- Image Restoration
- Layer Separation
- Attention Mechanism
- Benchmark Dataset
one_liner: 利用事件相机微动态信号破解反射/透射层歧义，实现SOTA级图像反射去除效果
practical_value: '- 主要是学术贡献，电商/推荐/Agent核心业务可借鉴点有限

  - 若业务涉及商品图去反光、多模态内容预处理，可参考引入额外模态信号破解单模态歧义的思路

  - 针对标注数据稀缺的CV类任务，可优先搭建符合真实场景规则的仿真数据生成管线降低标注成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有单帧图像反射去除方法依赖静态图像先验，反射层与透射层存在天然歧义，处理后残留大量伪影，同时该任务缺乏真实场景标注基准数据集。
### 方法关键点
1. 引入事件相机捕捉的微动态信号，利用反射层与透射层的差分运动特征破解层分离歧义
2. 构建EvReflection网络，包含微动力学解耦模块从事件流中提取各层专属运动先验，引导视差注意力整流模块去除RGB图像伪影
3. 开发视差感知仿真数据生成管线，构建该任务首个真实场景基准数据集EVR²
### 关键结果
在合成、真实场景基准数据集上均达到SOTA性能，PSNR分别较当前最优方法高出1.6dB、1.2dB以上
