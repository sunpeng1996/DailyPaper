---
title: Do Personality-Tuned LLMs Make Better Social Agents?
title_zh: 人格微调的大语言模型能否成为更优的社交智能体？
authors:
- Tim Krabbe
- Xiaodan Shi
affiliations:
- Department of Computer and Systems Sciences, Stockholm University
arxiv_id: '2609.21857'
url: https://arxiv.org/abs/2609.21857
pdf_url: https://arxiv.org/pdf/2609.21857
published: '2026-09-18'
collected: '2026-09-21'
category: Agent
direction: LLM驱动社交Agent · 人格微调
tags:
- Social Agent
- LoRA
- LLM Fine-tuning
- MBTI
- LLM-as-a-Judge
one_liner: 对比人格微调与指令提示的小开源LLM，发现前者未提升人格角色扮演一致性，且评估信度较低
practical_value: '- 做拟人化用户仿真、客服Agent人格定制时，优先测试指令Prompt方案，不要盲目上人格微调，小开源LLM的微调收益可能为负

  - 做主观类生成效果评估（如人格一致性、文案风格匹配）时，必须先验证多LLM评委的 inter-rater agreement，低于0.6的结论不可信

  - 若要提升生成文本的多样性，对Qwen系列小模型可尝试小参数LoRA微调，实测Distinct-2可提升约0.125

  - 垂直场景微调需重点做好数据域对齐，用社交媒体数据微调对话模型会存在域偏移，效果反而下降'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM广泛应用于社交智能体、多智能体仿真、用户模拟等场景，但现有模型生成的对话虽然流利，却缺乏稳定的行为特征，存在明显的“非人类陌生感”，可控性差。业界普遍认为人格感知微调是解决该问题的方案，但小参数量开源LLM的人格微调收益，以及和纯指令提示的效果对比尚未被系统验证。
### 方法关键点
- 模型选择Qwen2.5-7B-Instruct、Ministral-8B-Instruct两款小参数量开源LLM，用两组LoRA配置（r=16/α=32、r=32/α=64）进行微调，目标模块覆盖注意力层q/k/v/o投影
- 训练数据集融合Kaggle MBTI标注社交媒体帖子与DailyDialog多轮对话数据，用RoBERTa分类器为对话数据打MBTI标签，通过回译过采样缓解类别不平衡，最终共58.2万条样本
- 评估采用3种不同紧急度的对话场景，引入3个不同架构的LLM作为评委，结合定性编码和MBTI分类评估人格保真度，用Krippendorff's α衡量评委一致性，用Distinct-1/2衡量文本多样性
### 关键结果
- 人格保真度：基线模型的MBTI分类F1显著高于微调模型，Ministral基线F1范围0.595~0.820，Qwen基线F1范围0.530~0.791，微调模型F1平均低0.07~0.1
- 评估信度：整体评委Krippendorff's α最高仅0.654，远低于0.8的可信阈值，N/S维度一致性最低仅0.024，结果置信度低
- 文本质量：Qwen微调后Distinct-2提升约0.125，英文输出占比从88.35%提升至92%以上，文本多样性显著改善

**最值得记住的结论**：在未做好数据域对齐和评估信度验证的前提下，对小开源LLM做人格微调的效果不如直接使用基线模型的指令提示。
