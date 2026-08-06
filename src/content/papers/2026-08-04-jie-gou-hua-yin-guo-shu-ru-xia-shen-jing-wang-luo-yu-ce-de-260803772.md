---
title: Computing Actual Causes for Neural Network Predictions under Structured Causal
  Inputs
title_zh: 结构化因果输入下神经网络预测的实际成因计算
authors:
- Jannick Strobel
- Muqsit Azeem
- Stefan Leue
affiliations:
- University of Konstanz
arxiv_id: '2608.03772'
url: https://arxiv.org/abs/2608.03772
pdf_url: https://arxiv.org/pdf/2608.03772
published: '2026-08-04'
collected: '2026-08-06'
category: Reasoning
direction: 因果推理 · 神经网络预测可解释
tags:
- Causal Inference
- SCM
- Model Explainability
- Bound Propagation
- Branch and Bound
one_liner: 基于布尔SCM与分支定界等技术计算NN预测的HP实际成因，解决输入依赖下解释误导问题
practical_value: '- 推荐/广告排序的特征归因环节可引入布尔SCM建模特征间因果依赖，避免产生14%左右的虚假归因结论，提升归因可信度

  - 大规模特征归因计算可复用边界传播+分支定界的组合方案，相比暴力搜索、ILP baseline大幅提升计算效率，降低算力开销

  - 生成推荐可解释文案时，可借鉴HP实际成因框架输出符合真实因果逻辑的解释，避免不符合常识的解释误导用户'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有神经网络解释方法默认输入特征独立，当输入存在结构化因果依赖时会生成误导性、虚假归因结果，无法定位预测的真实根因。
### 方法关键点
将解释形式化为Halpern-Pearl(HP)实际成因，采用布尔结构因果模型(SCM)建模输入依赖关系，结合边界传播与分支定界技术计算HP成因，同时提供完备性与最小性的正式保证。
### 关键结果
性能显著优于暴力搜索、ILP baseline，图规模增大时效果超过启发式搜索；180s单实例时限内，可在最高28节点的SCM上，完成搜索空间最高$2.3\times10^{13}$的（成因、contingency）对的全部最小实际成因计算；案例验证忽略输入依赖会多生成14.9%的虚假成因。
