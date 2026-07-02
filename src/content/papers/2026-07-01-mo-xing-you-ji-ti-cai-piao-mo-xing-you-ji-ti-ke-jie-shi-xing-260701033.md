---
title: 'The Model Organism Lottery: Model Organism Interpretability Strongly Depends
  on Training Methodology'
title_zh: 模型有机体彩票：模型有机体可解释性高度依赖训练方法
authors:
- Andrzej Szablewski
- Gabriel Konar-Steenberg
- Raffaello Fornasiere
- Nikita Menon
- Stefan Heimersheim
affiliations:
- LASR Labs
- University of Cambridge
arxiv_id: '2607.01033'
url: https://arxiv.org/abs/2607.01033
pdf_url: https://arxiv.org/pdf/2607.01033
published: '2026-07-01'
collected: '2026-07-02'
category: LLM
direction: LLM可解释性 · 测试基准有效性验证
tags:
- Mechanistic Interpretability
- Model Organism
- SFT
- DPO
- Benchmark
one_liner: 通过54组不同训练配置的MO实验，证明现有可解释性测试代理MO的有效性存疑
practical_value: '- 做LLM4Rec/Agent安全审计时，避免仅用post-hoc SFT生成的恶意行为测试集，需补充训练阶段嵌入不良数据的测试样例，防止高估可解释性工具的检测能力

  - 微调业务域LLM（如电商文案生成、导购Agent）时，若要降低隐式违规行为被逆向提取的风险，可将特殊行为数据融入预训练后DPO阶段而非单独做SFT，提升行为隐蔽性

  - 自研LLM可解释性检测工具时，需基于多训练范式生成的测试MO做交叉验证，避免评估结果虚高'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前用于评估白盒可解释性技术的模型有机体（MO）多采用post-hoc SFT构建，过往研究显示这类MO的隐藏行为极易被检测，但有观点认为这类训练方式人为降低了可解释性难度，测试结果不具备实际参考性。
### 方法关键点
基于OLMo2-1B、gemma-3-1b-it两个基座，用7种不同训练方法（含标准post-hoc SFT、post-hoc DPO、将MO数据融入OLMo训练后DPO阶段的集成训练等）构建了54个MO样本集，对激活预言机、激活控制、logit lens、稀疏自编码器四类可解释性方法做基准测试。
### 关键结果
1. MO可解释性与训练目标、目标行为、模型架构、训练数据生成流程强相关；
2. 即使控制目标行为表达强度一致，可解释性结果仍存在显著方差；
3. 更贴合真实场景的集成训练生成的MO，可解释性远低于标准post-hoc方法构建的MO，现有MO作为可解释性代理的有效性存疑。
