---
title: AIMO Interpretability Challenge
title_zh: AIMO可解释性挑战赛
authors:
- Michal Štefánik
- Philipp Mondorf
- Andreas Waldis
- Qianying Liu
- Chuan Yang
- Michal Spiegel
- Josef Kuchař
- Marek Kadlčík
- Adam Vawda-Oomerjee
- Chaoran Liu
arxiv_id: '2607.13899'
url: https://arxiv.org/abs/2607.13899
pdf_url: https://arxiv.org/pdf/2607.13899
published: '2026-07-15'
collected: '2026-07-17'
category: Reasoning
direction: 大模型推理可解释性与鲁棒性评测
tags:
- interpretability
- reasoning robustness
- mathematical reasoning
- LLM evaluation
- benchmark
one_liner: 推出面向前沿数学大模型的可解释性竞赛，区分稳健推理与伪推理，配套数据集与算力支持
practical_value: '- 可借鉴「基于问题扰动生成功能变体」的思路，评测Agent推理模块鲁棒性，避免大模型依赖shortcut输出错误决策

  - 可复用「不唯最终准确率、优先校验内部推理机制可靠性」的评估逻辑，优化LLM驱动的搜索/推荐系统正确性校验流程

  - 构建LLM4Rec相关评测集时，可参考其对抗鲁棒性benchmark构建方法，规避模型过拟合训练数据伪关联的问题'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有标准推理基准仅通过最终答案准确率评估模型能力，无法区分模型是依赖稳定的推理机制，还是利用脆弱的推理捷径得到正确结果，无法验证模型决策的泛化性与可靠性。
### 方法关键点
基于AI数学奥赛（AIMO）题库与提交结果，结合Fields Model Initiative资源，竞赛提供三类核心支持：1）新发布的奥赛级数学推理题及符号化表示，支持生成功能等价的问题变体；2）前沿推理模型访问权限；3）模型在问题集上的对抗鲁棒性评估结果，配套算力基础设施支持参赛者开发稳健推理模型识别方法。
### 关键结果
竞赛将产出开放的鲁棒性评测基准与基线系统，为数学推理与可解释性领域提供长期标准化评测基础。
