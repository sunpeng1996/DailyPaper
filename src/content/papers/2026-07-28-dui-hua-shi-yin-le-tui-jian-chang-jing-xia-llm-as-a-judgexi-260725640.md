---
title: LLM-as-a-Judge for Evaluating System Responses in Conversational Music Recommendation
title_zh: 对话式音乐推荐场景下LLM-as-a-Judge系统响应评估方法研究
authors:
- Seungheon Doh
- Bruno Sguerra
- Sergio Oramas
- Elena V. Epure
- Juhan Nam
affiliations:
- KAIST
- Deezer Research
- SiriusXM
- Idiap Research Institute
arxiv_id: '2607.25640'
url: https://arxiv.org/abs/2607.25640
pdf_url: https://arxiv.org/pdf/2607.25640
published: '2026-07-28'
collected: '2026-07-29'
category: Eval
direction: 对话推荐 · LLM-as-a-Judge评估优化
tags:
- LLM-as-a-Judge
- Conversational Recommendation
- Evaluation
- CRS
- Music Recommendation
one_liner: 首个实证验证对话推荐场景下LLM评审与人类评估的对齐度，给出落地优化指南
practical_value: '- 搭建对话推荐/生成式推荐的响应自动评估pipeline时，优先选择LLM-as-a-Judge而非BLEU、ROUGE或普通embedding相似度指标，对齐度可提升至少0.2以上

  - LLM评审prompt优先引入多轮对话历史（单维度提升对齐度0.1左右），评估解释质量时额外补充领域内in-context样例，用户profile增益有限可按需加入

  - 轻量级LLM评审（如GPT-5.4nano、Gemini-3.1-Flash-Lite）可达到不错的评估效果，适合规模化offline迭代，高优场景再切换到更大模型

  - 注意规避LLM评审的风格偏差：冗余长文本、过于华丽的措辞会干扰评分，可在prompt中加入内容实质优先的约束，降低表面特征影响'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
对话式推荐系统（CRS）的响应生成质量直接影响用户信任与满意度，但传统参考类评估指标（BLEU、ROUGE、普通embedding相似度等）依赖固定参考文本，无法适配开放回复的多样性，也无法捕捉对话上下文、用户偏好与推荐理由的匹配性；人工评估成本高、难规模化，而LLM-as-a-Judge在CRS场景下的对齐度缺乏实证验证，其可靠性与优化路径尚不明确。
### 方法关键点
- 采样20条多轮音乐推荐对话，用4个不同规模的指令微调LLM生成共80条候选响应，覆盖不同质量层级
- 设计两类评估维度：个性化质量（响应对用户偏好、历史的匹配度）、解释质量（推荐理由和物品属性、用户需求的关联度）
- LLM评审输入包含对话历史、用户profile、待评响应、评估rubric与in-context样例，对比5款不同规模LLM评审、4类传统参考类指标、1类无参考embedding指标
- 招募20位音乐领域专家标注400份评分作为金标准，用bootstrap的皮尔逊、斯皮尔曼相关系数衡量对齐度
### 关键结果数字
- 所有LLM-as-a-Judge配置均显著优于基线：最优大模型（Gemini-3.1Pro）个性化维度皮尔逊r=0.55，解释维度GPT-5.4达到r=0.51；轻量模型（GPT-5.4nano）也能达到r≈0.4，比最优参考基线（r=0.19）提升超0.2
- 消融实验显示：加入对话历史可提升个性化维度对齐度0.13，in-context样例可提升解释维度对齐度0.08，用户profile增益仅0.02可忽略
- 偏差分析：LLM评审可抵御语义反转、prompt injection攻击，但对冗余长文本、华丽措辞存在一定评分偏差

**最值得记住的一句话**：LLM-as-a-Judge是目前对话推荐响应评估的最优规模化方案，但高优场景仍需搭配人工抽检，规避风格偏差与有限对齐度的影响。
