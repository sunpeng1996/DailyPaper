---
title: Identically Trained Language Models Break on Different Jailbreaks
title_zh: 相同训练配置的大语言模型对越狱攻击的易感性存在显著差异
authors:
- Chi-Wei Chang
- Mu-Tien Kuo
- Kuan-Wei Lee
- Meng-Hsun Tsai
affiliations:
- Cerulean Labs
- National Taiwan University
- National Yang Ming Chiao Tung University
arxiv_id: '2610.34074'
url: https://arxiv.org/abs/2610.34074
pdf_url: https://arxiv.org/pdf/2610.34074
published: '2026-10-24'
collected: '2026-11-06'
category: LLM
direction: LLM安全 · 预训练随机性影响越狱易感性
tags:
- LLM Safety
- Jailbreak Attack
- Pretraining Randomness
- Safety Alignment
- Model Fingerprinting
one_liner: 证实LLM越狱脆弱性更多由预训练随机过程决定而非训练数据
practical_value: '- 部署电商导购、客服类Agent时，安全对齐测试不能仅覆盖单个checkpoint，需多测几个不同预训练/微调种子的同配置模型，避免单一版本特有的越狱漏洞漏测引发合规风险

  - 做自有Agent的红队测试时，不要直接复用公开的、在其他模型上有效的越狱攻击模板，这些模板在你的部署模型上的有效率不足30%，必须针对实际部署的具体模型做定制化攻击测试

  - 若需要对线上部署的LLM服务做版本溯源、知识产权保护，可利用50条左右的定制越狱prompt的非拒绝率作为模型指纹，识别准确率可达98%，实现低成本、高准确率的模型溯源'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
过往LLM越狱评估默认模型的脆弱性完全由预训练数据、安全对齐策略决定，忽略了预训练过程本身的随机性影响。已有研究证实同配置不同种子训练的模型在下游预测精度、偏见水平上存在明显差异，但从未验证过越狱脆弱性是否也受预训练随机过程的独立影响，这会导致单一checkpoint的安全评估结论存在严重偏差。
### 方法关键点
- 基于25种公开预训练数据配方，每种配方用3个不同预训练种子训练1B参数量的Base模型，每个Base模型再用2个后训练种子执行完全相同的SFT+DPO安全对齐流程，累计生成150个对照模型；
- 整合HarmBench、WildJailbreak等7个公开基准的3212条越狱prompt，每个模型对每条prompt采样20次回复，用WildGuard标注非拒绝率，计算不同模型间非拒绝率的皮尔逊相关系数；
- 设计四类对照组合：同Base模型不同后训练种子（MZ双胞胎组）、同数据配方不同预训练种子组、跨数据配方组、同预训练种子不同硬件环境重跑组，拆分不同变量的影响权重。
### 关键结果
- MZ双胞胎组的非拒绝率相关系数达0.984，同数据配方不同预训练种子组的相关系数仅0.811，跨数据配方组的相关系数仅略降至0.779，说明越狱脆弱性对预训练运行的依赖度是训练数据的5.4倍；
- 同数据配方下，单模型上最优的攻击模板切换预训练种子后仅有27%仍保持最优，切换后训练种子则有67%仍最优；
- 仅需50条随机越狱prompt的非拒绝率作为特征，就能识别模型所属的预训练运行，准确率达98%。
### 核心结论
你在单个LLM checkpoint上挖到的越狱漏洞、测出的安全属性，大概率只是该特定预训练运行的特有产物，不能完全代表同数据同配置训练的所有模型的安全水平。
