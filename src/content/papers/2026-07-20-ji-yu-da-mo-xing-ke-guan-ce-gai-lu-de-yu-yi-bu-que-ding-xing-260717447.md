---
title: Calibrating Semantic Uncertainty from Observable Language-Model Probabilities
title_zh: 基于大模型可观测概率的语义不确定性校准方法
authors:
- Matthew F. Dixon
affiliations:
- Artificial Intelligence Finance Institute (AIFI)
- Quiota LLC
arxiv_id: '2607.17447'
url: https://arxiv.org/abs/2607.17447
pdf_url: https://arxiv.org/pdf/2607.17447
published: '2026-07-20'
collected: '2026-07-21'
category: LLM
direction: 大模型语义不确定性校准框架
tags:
- LLM Calibration
- Semantic Uncertainty
- Posterior Estimation
- Prompt Robustness
- Probability Alignment
one_liner: 提出语义映射框架，将LLM可观测短语概率转换为与提示措辞无关的业务状态校准后验
practical_value: '- 电商/推荐场景中，LLM生成推荐理由、商品分类、用户意图识别时，可预定义同义表达到业务标签的语义映射，合并对应token概率后再校准，大幅降低提示措辞波动导致的输出不稳定问题

  - Agent决策链路的不确定性量化，无需依赖LLM自报的置信度，通过计算相关语义短语的总概率结合少量标注校准，即可得到可审计的业务状态后验概率，降低决策幻觉风险

  - 业务效果调优可复用该方法的误差分解思路，拆分语义分组误差、概率计算误差、未覆盖语料占比三类问题，针对性优化链路，而非仅看最终准确率指标'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
当前LLM原生输出为token级概率，但金融、医疗、电商推荐等专业场景需要的是和业务语义状态绑定的稳定不确定性估计，LLM自报的置信度可靠性低，不同提示措辞会导致相同信息的输出大幅波动，无法直接用于可信决策，亟需可验证的方法将语言概率映射为语义不变的业务状态后验。

### 方法关键点
- 预定义语义映射规则，将同义短语分组映射到对应业务状态，计算每个状态下所有短语的概率总和，归一化得到语义层面的概率分布，保留未覆盖语料的质量占比作为误差项
- 拆分参考实验（业务状态真实后验）和语言实验（LLM输出概率），采用半参数推断建立两者的校准映射，推导了后验误差上界、语义映射的存在性、唯一性及提示扰动下的稳定性条件
- 提出三级误差分解框架，将最终后验误差拆分为语义分组误差、短语概率计算误差、未覆盖语料质量误差三类，可直接定位链路问题来源

### 关键实验
在美联储金融文本数据集和受控模拟数据集上测试，对比LLM直接输出的数值置信度基线，语义映射校准后的概率对预留样本后验的恢复准确率提升15%以上，95%置信区间覆盖率符合预期，同义改写提示下输出波动率下降40%，仅证据顺序调整仍会带来一定波动。

**最值得记住的一句话**：prompt engineering仅能优化措辞相关的响应，专业场景落地需验证业务相关语义输出的稳定性，不可直接信任大模型自报的置信度
