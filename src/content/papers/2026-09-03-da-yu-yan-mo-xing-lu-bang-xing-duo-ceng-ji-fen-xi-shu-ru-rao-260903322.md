---
title: 'How Perturbations Propagate: A Multi-Level Analysis of Robustness in Large
  Language Models'
title_zh: 大语言模型鲁棒性多层级分析：输入扰动的传播机制研究
authors:
- Dun Li Chan
- Emily Liu
- Niyathi Allu
- Christian Hoang
affiliations:
- INTI International College Penang
- Independent Researcher
- FPT University
arxiv_id: '2609.03322'
url: https://arxiv.org/abs/2609.03322
pdf_url: https://arxiv.org/pdf/2609.03322
published: '2026-09-03'
collected: '2026-09-05'
category: LLM
direction: 大语言模型鲁棒性评估
tags:
- LLM Robustness
- Perturbation Analysis
- Interpretability
- Attention Head
- Adversarial Attack
one_liner: 从输出、隐层、注意力头三层分析扰动传播规律，验证单度量鲁棒性评估的局限性
practical_value: '- 做搜索query纠错、用户输入预处理的鲁棒性评估时，不要仅依赖输出结果，可加入隐层CKA相似度、本征维度变化作为辅助指标，避免漏判内部表征的扰动风险

  - 基于LLM的电商导购Agent、推荐理由生成模块优化时，可重点增强copying注意力头的抗扰动能力，实验显示其与token替换、乱序下的输出恢复度相关度达0.726、0.622

  - 做LLM对抗攻击防护时，HotFlip梯度引导的token替换比同位置随机替换造成的NLL高18%以上，需优先针对这类梯度引导的攻击做防御'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有LLM鲁棒性评估通常仅依赖输出行为指标，无法区分不同扰动对模型内部计算的差异化影响，也无法判断跨模型鲁棒性结论的通用性，甚至可能因单度量偏差得到误导性结论，无法支撑鲁棒性优化的精准决策。

### 方法关键点
- 覆盖6种自然/合成扰动：字符替换、键盘输入错字、随机token替换、词替换、同义词替换、token乱序，同时对比梯度引导的HotFlip对抗扰动与同位置随机替换的差异；
- 三层级评估体系：输出层采用NLL、生成结果归一化编辑距离，隐层采用CKA表征相似度、本征维度变化，组件层采用注意力头功能得分、激活补丁恢复度；
- 测试模型覆盖4个不同规模的GPT-2系列、2个不同规模的Qwen2.5系列模型，基准数据集为WikiText-2中随机抽样的300条长度≥128的序列。

### 关键结果
- 同类输出扰动可能对应完全不同的隐层变化，单靠输出度量的鲁棒性评估漏判率高；copying注意力头与token替换、乱序下的输出恢复度相关度最高，分别为0.726、0.622；
- HotFlip对抗扰动比同位置随机替换在所有测试模型上NLL高18%-30%，输出发散度高33%以上，内部表征相似度更低；
- GPT与Qwen系列的扰动响应在输出层差异<7%，但隐层本征维度变化差异可达20%以上。

**最值得记住的结论**：仅基于单一行为或表征度量的鲁棒性结论具有误导性，需多维度度量收敛验证才能得到可靠结果。
