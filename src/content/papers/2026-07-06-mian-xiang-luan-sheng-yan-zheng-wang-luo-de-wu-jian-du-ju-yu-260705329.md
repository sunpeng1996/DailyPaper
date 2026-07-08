---
title: How Far is Too Far? Defining the Distance Threshold for Verification Siamese
  Networks
title_zh: 面向孪生验证网络的无监督距离阈值定义方法
authors:
- Heloísa Dias Viotto
- Cauê Samonek
- Lucas Garcia Pedroso
- Marcos Sunye
- André Abed Grégio
- Paulo Lisboa de Almeida
affiliations:
- Departamento de Informática (DInf), Universidade Federal do Paraná
- Departamento de Matemática (DMAT), Universidade Federal do Paraná
arxiv_id: '2607.05329'
url: https://arxiv.org/abs/2607.05329
pdf_url: https://arxiv.org/pdf/2607.05329
published: '2026-07-06'
collected: '2026-07-08'
category: Other
direction: 孪生网络 · 无监督阈值确定
tags:
- Siamese Network
- Unsupervised Learning
- Embedding Matching
- Threshold Optimization
- Verification Task
one_liner: 提出无标注依赖的孪生验证网络距离阈值确定方法，性能与等错误率方法相当
practical_value: '- 电商同款商品匹配场景可复用该方法，无需标注就能快速确定孪生匹配网络的阈值，降本提效

  - 推荐/搜索召回阶段embedding相似度阈值动态调整，新类目/新场景上线时无需标注即可快速适配

  - 用户兴趣embedding匹配、跨域item匹配等任务可基于该方案实现阈值的在线自动更新，降低人工维护成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
孪生验证网络广泛应用于embedding匹配、同类判定任务，判断样本是否同类的距离阈值通常依赖标注数据确定，标注成本高，无法支持部署后的动态在线更新。
### 方法关键点
假设孪生网络输出的样本间距离分布符合双峰特性，通过无监督定位两个分布峰之间的最小值点作为判定阈值，全程无需标注样本，可直接在部署环境下动态更新阈值。
### 关键结果
在MNIST、CIFAR-10、LFW、PKLot四个数据集上平均验证准确率达94%，性能与需要标注数据的等错误率（EER）方法相当，完全省去阈值确定环节的标注成本。
