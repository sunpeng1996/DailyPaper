---
title: 'Auditing the Judge: Internal Signals for LLM Reasoning Assurance'
title_zh: 审计LLM自判决：基于内部激活信号的推理可信度保障方法
authors:
- Mayank Gulati
- Gerhard Wunder
affiliations:
- Freie Universität Berlin
arxiv_id: '2611.14323'
url: https://arxiv.org/abs/2611.14323
pdf_url: https://arxiv.org/pdf/2611.14323
published: '2026-11-10'
collected: '2026-11-11'
category: LLM
direction: LLM推理保障 · 内部激活探针
tags:
- LLM_reliability
- internal_probe
- self_judgment
- error_detection
- selective_prediction
one_liner: 基于LLM自判决阶段注意力头激活训练探针，固定预算下错误召回显著优于黑盒自判决分数
practical_value: '- 电商/广告Agent的应答、文案生成质量校验场景，可复用「自判决阶段注意力头激活+轻量MLP探针」架构，替代单纯的LLM自评分，5%审核预算下就能多捕获1.3%以上的错误，降低不良内容流出率

  - 做生成式推荐、LLM驱动的query改写的质量管控时，不要用AUROC作为上线核心指标，要基于业务可承担的审核/重生成预算做定点效果验证，优先保证低预算下的错误召回率

  - 跨业务场景迁移错误检测探针时不可直接复用，必须用目标场景的标注数据重新训练或校验，无标注时优先用原生LLM自判决分数作为fallback，避免性能大幅下降'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM系统普遍依赖自判决决定输出是否释放、复审或重算，而人工审核、额外推理算力的预算非常有限；传统AUROC指标是全预算区间的平均效果，无法反映实际部署时低预算场景的错误捕获能力，黑盒自判决的连续token分数会丢失内部状态中大量与错误相关的信息，亟需适配固定预算的高效错误检测方案。
### 方法关键点
- 对比两类错误打分信号：黑盒基线为自判决阶段YES/NO token的连续概率p(YES)，白盒探针为基于自判决阶段最终位置注意力头激活训练的监督分类器
- 训练阶段先用Fisher可分性筛选训练集中与错误相关性最高的32个注意力头，拼接激活特征后训练5种子的MLP集成作为最终探针
- 核心评估指标为固定复审/算力预算下的错误召回率、未复审输出的剩余错误率，而非全局AUROC
### 关键结果
- 实验覆盖GSM8K、MATH两个数学推理数据集，3个7-12B开源指令微调模型（Gemma 3 12B、Qwen2.5 7B、Llama 3.1 8B）
- 5%复审预算下，探针在所有6组模型-数据集配置中比自判决多捕获1.3~22.5个百分点的错误，中位数为7.4个百分点，对应未复审输出的错误率下降0.38~2.01个百分点
- 10%算力路由预算下，探针引导的额外推理分配准确率均优于随机分配，仅在自判决效果较差的场景下优于自判决引导的路由
- 跨数据集迁移时探针AUROC下降0.04~0.27，泛化性差
### 核心结论
保障效果由实际部署的预算点决定，而非全局AUROC；内部信号仅在有监督的域内场景能提升预算分配效率，不是通用的置信度估计器
