---
title: 'Support-Compiled Feature Folding: More Evidence at Lower Memory Across Tabular
  Foundation Models'
title_zh: 支持度编译特征折叠：低内存开销下保留表格大模型特征证据
authors:
- Tian Zhou
- Beverly Jin
- Xue Wang
- Linxiao Yang
- Wenwei Wang
- Bingqing Peng
- Mengni Ye
- Jinjie Gu
- Liang Sun
affiliations:
- Ant Group
- Independent Researcher
arxiv_id: '2609.28208'
url: https://arxiv.org/abs/2609.28208
pdf_url: https://arxiv.org/pdf/2609.28208
published: '2026-09-23'
collected: '2026-09-24'
category: Training
direction: 表格基础模型 · 推理内存优化
tags:
- Tabular Foundation Model
- Inference Optimization
- Memory Reduction
- Feature Folding
- Training-Free
one_liner: 提出无需训练的SCFF推理框架，解决表格基础模型特征缩放的内存与精度权衡问题
practical_value: '- 电商推荐宽表特征推理可直接复用SCFF框架，无需微调现有表格大模型主干，即可将GPU内存占用降低2倍以上，同时保留更多特征避免精度损失

  - 特征排序+分块编码+结果融合的链路可迁移至召回/排序阶段的高维特征处理场景，解决特征交互二次方复杂度瓶颈

  - 内存受限的端侧/边缘推荐部署场景，可借鉴SCFF的固定工作集设计，在算力上限内保留更多有效特征提升推荐精度'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
表格基础模型存在特征侧缩放两难：全宽度特征两两交互的复杂度随列数二次增长，而特征选择方案会丢弃有效特征导致精度下降，无法兼顾内存开销与效果。
### 方法关键点
提出训练免的SCFF推理框架，无需修改冻结模型主干：1）按支持度排序特征，通过原生特征编码器的有限叶子节点路由；2）对残差特征做支持度校验；3）在上下文预测前合并编码后的特征消息，将二次方特征交互复杂度转为线性，无需集成预测或训练新参数。
### 关键结果
在AMLB-29、TabZilla等18个宽表数据集上，6类测试主干的精度、NLL均有提升；匹配宽度对比下相对误差降低最高26.1%；GPU内存中位数节省2.09~2.36x，峰值内存最高降低34.3x；固定内存上限下，精度比单叶子编码器最优方案提升3.72~4.06个百分点。
