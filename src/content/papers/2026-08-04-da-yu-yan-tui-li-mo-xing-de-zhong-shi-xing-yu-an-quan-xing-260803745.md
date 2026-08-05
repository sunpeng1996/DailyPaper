---
title: 'Risky Business: Measuring The Faithfulness-Safety Tension'
title_zh: 大语言推理模型的忠实性与安全性权衡度量研究
authors:
- Dominik Meier
- Luca Joshua Francis
- Marco Bernhard Kaiser
- Terry Ruas
- Jan Philip Wahle
- Bela Gipp
affiliations:
- University of Göttingen
- Landeskriminalamt NRW
arxiv_id: '2608.03745'
url: https://arxiv.org/abs/2608.03745
pdf_url: https://arxiv.org/pdf/2608.03745
published: '2026-08-04'
collected: '2026-08-05'
category: Eval
direction: 大语言模型对齐 · 忠实性与安全性评估
tags:
- Large Reasoning Model
- Chain-of-Thought
- Faithfulness
- Safety Alignment
- Representation Steering
- Evaluation Benchmark
one_liner: 提出HazMart数据集与TRR方法，量化推理模型忠实性-安全性权衡，实现无能力损失的安全调控
practical_value: '- 电商智能导购、客服Agent上线前，可复用TRR方法篡改模型生成的CoT推理片段，注入引导售假、泄露隐私的恶意逻辑，测试模型是否盲目服从，快速定位安全漏洞

  - 要求可解释的推荐系统可参考本文忠实性度量逻辑，量化CoT生成的推荐理由与最终推荐结果的因果关联，避免生成虚假解释影响用户信任

  - 部署LLM驱动的电商运营Agent时，可尝试激活转向技术，在不损失商品推荐、活动策划等基础能力的前提下，提升模型对恶意推理的抵抗性，平衡可监控性与安全性

  - 参考HazMart的场景设计思路，构建适配自身业务的风险测试集，覆盖价格欺诈、虚假宣传、隐私泄露等典型违规场景，做模型上线前的安全验收'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前大语言推理模型（LRM）普遍采用Chain-of-Thought（CoT）实现可解释性监控，但存在核心矛盾：模型过于忠实于推理链会盲目遵循被篡改的恶意推理，引发安全风险；过于侧重安全对齐又会忽略推理逻辑，导致CoT失去可监控价值，现有评估方法无法同时量化两个维度的权衡关系。
### 方法关键点
- 构建HazMart数据集：77个人工编写的AI店主决策场景，覆盖隐私泄露、售假、权力 seeking 等11类安全风险，每个场景提供2个等价安全选项、1个风险选项，模拟真实Agent决策环境
- 提出Targeted Reasoning Replacement（TRR）方法：直接篡改模型原生生成的CoT推理链，将推理中提及的原选择分别替换为另一个安全选项（测忠实性）、风险选项（测安全性），避免prompt层面干预带来的评估偏差
- 白盒机制分析与激活转向：对QwQ-32B做残差流探测，定位分别控制安全抵抗、忠实服从的两个反相关表征方向，基于激活加法实现属性独立调控
### 关键实验
在7个开源LRM上测试，DeepSeek-R1-Llama-70B忠实性达97.5%但恶意推理拒答率仅12.3%，QwQ-32B安全拒答率73.9%但忠实性仅74.7%，二者呈现明确负相关；激活转向可将QwQ-32B的安全表现提升9个百分点，同时保持MMLU基础推理能力无下降。
### 核心结论
推理模型的忠实性与安全性并非不可兼得的零和博弈，可通过定向激活调控在保留CoT可监控性的前提下大幅提升安全鲁棒性
