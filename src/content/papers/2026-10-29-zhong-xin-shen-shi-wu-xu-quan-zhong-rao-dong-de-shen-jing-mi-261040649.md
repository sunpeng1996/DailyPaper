---
title: Rethinking Neural Thickets Without Weight Perturbations
title_zh: 重新审视无需权重扰动的神经密丛效应机制
authors:
- Nicolas Dufour
- Elouan Gardès
- Amil Dravid
- Patrick Pérez
- Loic Landrieu
affiliations:
- Kyutai
- Meta FAIR
- LIGM, CNRS
- UC Berkeley
- Google DeepMind
arxiv_id: '2610.40649'
url: https://arxiv.org/abs/2610.40649
pdf_url: https://arxiv.org/pdf/2610.40649
published: '2026-10-29'
collected: '2026-10-30'
category: LLM
direction: LLM推理优化 · 无训练适配
tags:
- Logit Perturbation
- Test-time Adaptation
- Ensemble Learning
- Neural Thickets
- Inference Optimization
one_liner: 提出仅扰动输出logit的PSV方法，无需权重改动即可追平原神经密丛方案的性能
practical_value: '- 电商场景的LLM文案生成、商品推理类任务可直接复用Logit PSV：无需微调模型，仅在输出logit上加固定高斯偏置，经百级样本的小验证集筛选后投票，即可提升推理准确率，比全权重扰动节省90%以上的内存与计算开销

  - 垂域推理任务（如优惠规则计算、合规校验）若基模效果达标，可优先尝试「温度采样+多数投票」的轻量方案，无需引入验证选择逻辑，进一步降低推理复杂度，适配低延迟线上场景

  - 跨域推荐/分类的分布偏移问题，可借鉴Logit扰动+验证校准思路，无需重训backbone，仅在输出层做扰动筛选即可快速提升跨域性能，尤其适合冷启动垂域的快速适配需求'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
神经密丛（Neural Thickets）假说提出预训练大模型权重空间周围存在大量任务专属专家，通过随机高斯扰动全量权重可大幅提升推理性能，但该方案计算成本极高，且性能增益的底层机制未被清晰解释，亟需轻量化等效方案与明确的机制解读。
### 方法关键点
- 构建统一Perturb-Select-Vote（PSV）框架，将原神经密丛方法归为全权重扰动的PSV特例，核心流程为：生成多份扰动预测器、小验证集筛选TopK高性能成员、测试时投票聚合结果
- 提出Logit PSV轻量化方案：完全冻结模型权重，仅在输出logit上添加固定高斯偏置，同一偏置在所有解码步骤、所有输入中保持不变，无需修改模型内部结构或参数
- 一阶分析验证：小权重扰动的核心作用本质是诱导logit偏移，因此直接在输出层注入等效扰动即可复现全权重扰动的性能增益
### 关键实验结果
语言任务上，在0.5B-7B尺度模型的7类推理任务测试，Logit PSV在MATH-500任务上将准确率从63.3%提升至81.3%，超过全权重PSV的74.7%；GSM8K准确率从87.5%提升至91.9%，超过全权重PSV的89.8%；15个推理任务中13个性能追平或超过全权重PSV。
视觉域偏移场景下，Logit PSV在FMoW、Waterbirds数据集上相比基线分别提升6.2、5.0个百分点的最差域/组准确率，远超过全权重PSV的1.0、0.3个百分点增益。
### 核心结论
神经密丛的性能增益本质来自输出多样性、验证筛选和投票聚合，无需依赖权重空间的局部专家结构，仅通过输出层扰动即可低成本获得等效甚至更优的效果
