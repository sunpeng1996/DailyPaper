---
title: 'On-Policy Distillation for LLM Safety: A Routing Approach to Template-Robust
  Realignment'
title_zh: 基于路由的On-Policy蒸馏框架：实现模板鲁棒的LLM安全重对齐
authors:
- Yongjian Guo
- Wanlun Ma
- Lingyu Shen
- Xi Xiao
- Sheng Wen
affiliations:
- Tsinghua University
- Swinburne University of Technology
- EPFL
arxiv_id: '2607.27081'
url: https://arxiv.org/abs/2607.27081
pdf_url: https://arxiv.org/pdf/2607.27081
published: '2026-07-29'
collected: '2026-07-30'
category: LLM
direction: LLM安全 · 重对齐蒸馏优化
tags:
- LLM Safety
- Knowledge Distillation
- On-Policy Distillation
- Alignment
- Robustness
one_liner: 提出双教师路由的On-Policy蒸馏架构，实现兼顾任务保留与跨模板鲁棒的LLM安全重对齐
practical_value: '- 垂直领域Agent（电商客服、广告文案生成等）安全加固可复用双教师蒸馏架构：用原安全对齐LLM做安全教师，微调后的领域专家模型做任务教师，既能保留领域能力又能降低有害输出，无需从零重训。

  - 蒸馏优化可采用top-K KL散度损失，仅对齐教师输出分布的头部概率+尾部聚合，大幅降低训练成本，避免全vocab计算冗余，适合业务侧快速迭代。

  - 安全加固后的LLM上线验收不能只测单一prompt模板，必须覆盖原生对话模板、极简模板、潜在攻击模板等多场景，避免被用户更换prompt绕过安全限制。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM安全重对齐方法存在三大缺陷：一是修复安全时会严重损失下游微调得到的专业能力，二是高度依赖已知攻击的prompt模板，模板不匹配时防御效果下降超30%甚至完全失效，三是修复后仍可通过更换系统提示词重新越狱，无法应对LLM供应链微调投毒的实际威胁。

### 方法关键点
- 双教师冻结蒸馏架构：安全教师为预攻击的原始对齐LLM，提供跨模板的拒绝输出先验；任务教师为被投毒的微调后模型，保留下游专业能力。
- 样本路由机制：按样本来源分配蒸馏目标，有害样本对齐安全教师的输出分布，任务样本对齐任务教师的输出分布，解耦安全与能力优化目标。
- 轻量化损失设计：采用top-K KL散度损失，仅对齐教师输出分布的top-K高概率token，剩余尾部概率聚合计算，降低大vocab下的蒸馏计算量。

### 关键实验
在Llama-2、Qwen2.5、Gemma-2三个基座，SQL、对话摘要、NL2Bash三个下游任务上，对比SSRD、RESTA、soft-SFT、rollback四个SOTA基线：模板不匹配时基线防御效果下降超30%，甚至任务性能降到0；ROPD跨模板ASR仅上升到19.7%，同时保留95%以上的下游任务性能，仅需1500条样本即可将ASR从62%降到2.4%，训练时间仅15分钟左右，远低于rollback等基线的开销。

所有LLM安全重对齐方法都是prompt条件性的，而非永久性的权重级修复，必须假设攻击者可自由修改prompt来设计防御体系。
