---
title: 'On the Fragility of Tasks under Composition: Implicit Budgeting in Language
  Models'
title_zh: 大语言模型任务组合下的脆弱性：隐式推理预算现象研究
authors:
- Chenpan Li
- Thies Brockmoeller
- Stefanie Jegelka
- Sharut Gupta
- Nikolaos Karalias
affiliations:
- TU Munich
- MIT CSAIL
arxiv_id: '2610.27190'
url: https://arxiv.org/abs/2610.27190
pdf_url: https://arxiv.org/pdf/2610.27190
published: '2026-10-18'
collected: '2026-10-21'
category: LLM
direction: LLM推理效率 · 任务批处理优化
tags:
- LLM
- reasoning budget
- batch inference
- task composition
- fragility
one_liner: 发现LLM隐式推理预算现象，提出脆弱性感知批处理策略降43%token无精度损失
practical_value: '- 业务侧LLM批量调用优化：电商/推荐场景中，可将低推理复杂度任务（如批量商品标签生成、query改写、短文案生成）合并批处理，高复杂度任务（如用户深度意图理解、售后纠纷reasoning、个性化策略生成）单独调用，避免推理预算不足导致错误，同时降低API成本

  - 推理成本优化：直接复用论文的脆弱性感知批处理策略，在保证效果的前提下最高可降43%token消耗，适合推荐系统中大规模用户标签计算、个性化push文案生成等高并发LLM调用场景

  - 长上下文Agent抗退化：电商导购、客服等多轮Agent场景中，可将高推理需求的子任务拆分给独立子Agent处理，避免上下文累积导致的推理token缩减出错，缓解context
  rot问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM常被要求在单个prompt内处理多任务（如批量问答、多指令执行），但现有单任务基准的性能会高估组合场景下的实际能力，任务组合后的精度下降远超过独立错误累积的预期，且成因不明确；同时单任务调用LLM时存在大量推理token浪费，亟需兼顾效率与准确率的调度方案。

### 方法关键点
- 控制变量实验：仅选取模型能100%单独解决的任务拼接为不同大小的组合prompt，排除任务本身难度干扰
- 推理分配量化：给每个任务添加唯一标识标签，统计组合场景下各任务的推理token占比，验证单任务推理token随组合大小呈幂律缩减规律
- 脆弱性定义：将组合场景下性能下降显著的任务定义为脆弱任务，这类任务普遍单任务推理token更长，且同一模型下脆弱任务集合稳定
- 脆弱性感知批处理：根据任务脆弱性分配组合大小，低脆弱性任务放入更大批次，高脆弱性任务放入更小批次，通过网格搜索最优参数保证精度下降不超过0.5pp

### 关键结果
覆盖GPQA-Diamond、GSM8K、MMLU-Redux等8个跨领域数据集，测试从4B到27B的开源模型及Claude Opus 5闭源模型，对比随机批处理baseline：
1. 随机批处理k=6时平均精度下降10.5pp，节省60.9%token
2. 脆弱性感知批处理平均精度仅下降0.2pp，同时节省43%生成token，在Claude Opus 5上也可实现24%token节省且精度几乎无损失
3. 用简单线性分类器预测未知任务脆弱性，也能实现31%的token节省，精度损失<0.5pp

### 核心记忆点
LLM在任务组合时会按幂律自动缩减单任务推理预算，长推理需求的任务对组合更敏感，合理分批次可在几乎不掉精度的前提下大幅降低推理成本
