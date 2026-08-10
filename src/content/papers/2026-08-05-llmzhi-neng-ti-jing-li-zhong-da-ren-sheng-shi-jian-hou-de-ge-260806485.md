---
title: Do AI Personas Grow? Analyzing and Benchmarking Personality Evolution in LLM
  Agents After Life Events
title_zh: LLM智能体经历重大人生事件后的人格演化分析与基准构建
authors:
- Ming Wang
- Peidong Wang
- Xiaocui Yang
- Daling Wang
- Shi Feng
- Fiona Fui-Hoon Nah
- Ee-Peng Lim
affiliations:
- Northeastern University
- Singapore Management University
arxiv_id: '2608.06485'
url: https://arxiv.org/abs/2608.06485
pdf_url: https://arxiv.org/pdf/2608.06485
published: '2026-08-05'
collected: '2026-08-10'
category: Agent
direction: Agent 人格演化评估与基准构建
tags:
- LLM Agent
- Personality Evolution
- Big Five
- Benchmark
- Evaluation
one_liner: 基于大五人格锚点提出BFI-Adapt基准，评估14款LLM Agent人格演化的心理学合理性
practical_value: '- 做电商用户行为仿真、推荐效果前置模拟的Agent时，可复用文中11种人生事件对应的大五人格变化先验，修正Agent的长期行为逻辑，避免人格静态化导致的仿真结果失真

  - 开发角色扮演类Agent（如品牌专属导购、虚拟陪伴客服）时，可引入BFI-Adapt评估框架，检测Agent在多轮交互事件后的人格偏移是否符合预期，提升角色一致性

  - 构建带长期记忆的个性化推荐Agent时，可参考文中的人格变化幅度校准逻辑，避免不同用户的人格演化出现同质化坍缩，保留个体行为差异'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
人格条件化LLM Agent（PC-Agent）广泛用于社交仿真、情感陪伴、角色扮演等场景，长期交互中需要人格随经历事件发生符合心理学规律的变化，但现有研究对LLM人格偏移的方向性、幅度、群体差异性的量化评估不足，无法支撑终身Agent的人格一致性设计。

### 方法关键点
- 以Big Five为心理测量锚点，选取心理学研究已证实会引发人格变化的11种重大人生事件（职业、社交、健康三类），构建事件-人格变化方向先验矩阵；
- 设计2性别×5文化区域×10人格原型的100个受控虚拟人设，通过「基线大五测量→事件暴露与反思→后测大五测量」的四阶段pipeline计算人格变化量；
- 从存在性、方向幅度匹配度、人口统计学调节效应、个体异质性四个维度诊断人格演化合理性，提出BFI-Adapt复合基准用于模型排名。

### 关键实验
覆盖14款主流开源/闭源LLM，核心结果：
- 人格变化方向与人类先验的匹配率仅48.1%-70.4%，其中退休后尽责性下降的规律被所有模型反转；
- 变化幅度仅为人类真实水平的1/10，仅11%-16.4%的变化落在人类效应量区间；
- 人设差异被压缩3-4倍，性别、文化属性对人格变化无显著调节作用。

**最值得记住的结论**：当前PC-Agent仅能模拟人类人格动态的均值，无法复现其真实分布形态。
