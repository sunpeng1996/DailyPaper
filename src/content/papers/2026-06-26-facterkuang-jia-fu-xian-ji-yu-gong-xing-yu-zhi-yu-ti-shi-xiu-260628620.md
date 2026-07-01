---
title: 'Reproducing FACTER: Fairness via Conformal Thresholding and Prompt Repair'
title_zh: FACTER框架复现：基于共形阈值与提示修复的LLM推荐公平性研究
authors:
- Oscar Miró López-Feliu
- Daimy van Loo
- Xanthos Kekkos
- Mikel Blom
- Clara Rus
affiliations:
- University of Amsterdam
arxiv_id: '2606.28620'
url: https://arxiv.org/abs/2606.28620
pdf_url: https://arxiv.org/pdf/2606.28620
published: '2026-06-26'
collected: '2026-06-30'
category: GenRec
direction: 生成式推荐 · 公平性干预
tags:
- Fairness
- LLM4Rec
- Conformal Prediction
- Prompt Engineering
- Reproducibility
one_liner: 复现LLM推荐公平性框架FACTER，验证其效果边界并提出静态公平提示基线
practical_value: '- 黑盒LLM推荐场景无需微调，直接添加静态公平提示即可达到与FACTER动态修复相当的公平性效果，省去在线监控、规则迭代的算力和维护成本

  - 若需合规可解释的公平性约束，可借鉴FACTER的「AVOID 群体→特征」规则注入模式，直接将监管要求转化为prompt规则落地

  - 生成式推荐落地优先选择约束重排范式，可避免开放生成的幻觉问题，实验中重排场景下NDCG@10从开放生成的0.03+提升至0.43+，效用提升10倍以上

  - 不要将自适应阈值统计的内部违规数作为公平性优化的唯一目标，该指标下降多源于阈值动态放宽，不代表全局公平性真实提升'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM已广泛应用于电商、内容推荐场景，但训练数据中蕴含的社会偏见会导致不同人口属性用户收到系统性差异的推荐结果，既损害用户体验，也带来合规风险。现有LLM推荐公平性方案大多依赖模型微调，无法适配黑盒API调用的主流部署场景。原FACTER框架宣称通过共形阈值校准和动态提示修复，可在几乎不损失推荐效用的前提下实现公平性提升，但公开实现细节存在多处模糊，可复现性存疑，其业务落地价值亟需验证。

### 方法关键点
- 1:1复现FACTER核心逻辑：离线阶段基于反事实邻居的推荐语义差异计算非一致性分数，校准初始公平阈值；在线阶段检测到阈值违规时，同时注入"AVOID 群体→特征"的规则到系统prompt，且通过指数平滑更新阈值
- 新增静态公平零样本基线：仅在系统prompt中加入通用公平要求，无动态调整逻辑，用来隔离动态修复模块的增量价值
- 新增约束重排任务范式：固定候选集包含相关物品和负样本，排除开放生成的hallucination和检索误差干扰，单独评估公平性机制的真实效果

### 关键结果
在MovieLens-1M、Amazon Movies&TV两个数据集上，覆盖Llama2-7B、Llama3-8B、Mistral-7B三个开源LLM，对比无公平干预的Neutral基线、静态公平提示基线、FACTER：
- 开放生成场景下复现效用远低于原论文宣称值，NDCG@10不足0.04；仅能验证FACTER可将自适应阈值下的内部违规数从42.7降到9.0（ML-1M），但CFR、SNSR等全局公平指标无显著提升
- 重排场景下推荐效用回归合理区间，Neutral基线NDCG@10达0.466，FACTER仅损失约6%的NDCG@10；静态公平基线的公平性表现与FACTER相当，动态修复无额外增益

### 核心结论
黑盒LLM推荐场景下，简单的静态公平提示即可覆盖大部分场景的公平性需求，复杂的动态修复机制边际效益极低，且自适应阈值的内部违规数下降不能等同于真实全局公平性的提升
