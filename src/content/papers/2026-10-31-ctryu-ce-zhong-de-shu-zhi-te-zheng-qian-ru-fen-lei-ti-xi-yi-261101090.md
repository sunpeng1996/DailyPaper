---
title: 'Numerical Embeddings for CTR Prediction: A Taxonomy, Unified Benchmark, and
  Open-Source FuxiCTR Extension'
title_zh: CTR预测中的数值特征嵌入：分类体系、统一基准与FuxiCTR扩展
authors:
- Heng Yao
- Hanwei Zhu
- Tianying Liu
- Yulou Shu
- Siyun Hou
affiliations:
- Ant Group
- Alibaba Inc.
- Henan Polytechnic University
- Independent Researcher
arxiv_id: '2611.01090'
url: https://arxiv.org/abs/2611.01090
pdf_url: https://arxiv.org/pdf/2611.01090
published: '2026-10-31'
collected: '2026-11-03'
category: RecSys
direction: CTR预测 · 数值特征嵌入测评
tags:
- CTR-Prediction
- Numerical-Embedding
- Benchmark
- FuxiCTR
- RecSys
one_liner: 首个面向CTR预测的数值嵌入开源基准，提供分类体系与统一测评框架
practical_value: '- 数值嵌入选型优先用DEER作为baseline，z-score预处理下平均排名3.41普适性最强，训练速度比基础Field方案快24%，仅推理延迟高20%，性价比突出

  - 数值嵌入方案必须和预处理规则绑定复用，固定配置下输入尺度切换会导致11/27的场景最优方案变更，甚至部分方案AUC掉至0.55以下，不要直接跨预处理迁移方案

  - 不要仅以参数量作为选型依据，DAE参数量36.7k但推理延迟仅为Field的1.13倍，NaryDis-Lite仅19k参数量却有2.26倍延迟，选型必须实测真实推理耗时

  - 可直接复用开源NumEmbBench工具链，基于FuxiCTR的插件接口快速测试自研数值嵌入方案，无需修改CTR主干网络代码，大幅降低测评成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
CTR预测任务中，价格、统计计数等数值特征的嵌入方案直接影响最终效果，但现有测评多混杂不同预处理规则、主干网络和训练流程，无法公平对比不同数值嵌入的真实性能，也缺乏标准化的开源测评工具支撑算法迭代。
### 方法关键点
- 构建6大类共18种数值嵌入的分类体系，按坐标构建机制分为点投影、离散化、固定基、分段基、自适应坐标、分布/上下文自适应6类，明确不同方案的核心差异
- 基于FuxiCTR实现统一插件接口，数值嵌入模块可直接插拔替换，无需修改DNN、DeepFM、DCNv2、AutoInt等9种主流CTR主干网络的代码
- 采用统一train-only z-score预处理协议，每个方案经同等算力调参后冻结配置，在3个数据集上用5个种子重复实验保证结果可靠，额外增设原生输入尺度赛道测试方案的跨预处理迁移性
### 关键结果
- 实验覆盖Criteo、AutoML-A、AutoML-E三个公开数据集，共完成2430组z-score赛道实验和2430组原生尺度赛道实验
- z-score赛道下DEER平均排名3.41最优，拿下14个场景第一、19个场景前三；共6种方案在至少1个场景夺冠，不存在通用最优解
- 原生尺度赛道下，11/27的场景最优方案发生变更，57个配置AUC跌至0.55以下，方案迁移性高度依赖数据分布
- 耗时方面DEER训练速度是基础Field方案的0.76倍，推理延迟仅为1.20倍；NaryDis系列方案推理延迟超Field的2倍，性价比偏低
### 核心结论
数值嵌入选型没有通用最优解，必须结合具体数据集、主干网络、预处理规则和业务的性能约束综合选择
