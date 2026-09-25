---
title: 'IterSynth: Rethinking Deep Search Agents via Role-Decoupled Iterative Synthesis'
title_zh: IterSynth：基于角色解耦迭代合成的深度搜索Agent范式
authors:
- Xingyu Wu
- Yuchen Yan
- Zhengxi Lu
- Siqi Chen
- Xin ZHANG
- Aiting Liu
- Chao Deng
- Jie Liu
- Jin Ma
- Jian Shao
affiliations:
- Zhejiang University
- Tencent
arxiv_id: '2609.29444'
url: https://arxiv.org/abs/2609.29444
pdf_url: https://arxiv.org/pdf/2609.29444
published: '2026-09-23'
collected: '2026-09-25'
category: Agent
direction: 搜索Agent · 角色解耦训练优化
tags:
- SearchAgent
- RoleDecoupling
- RDPO
- LongHorizonReasoning
- LLM
one_liner: 单LLM共享参数实现规划合成双角色解耦，搭配RDPO训练提升长时序深度搜索性能
practical_value: '- 业务侧做智能导购、多轮搜索等Agent时，可直接复用IterSynth的双角色Prompt范式，无需训练/改模型，仅通过角色提示拆分「需求挖掘/query生成」和「召回信息整合/用户画像更新」两个模块，零成本获得长路径交互性能提升，同时避免多Agent部署的额外开销

  - 训练共享参数的多角色Agent时，可直接复用RDPO的信用分配方案：为不同角色设计专属rubric评分，拆分奖励池独立计算优势，避免不同任务的奖励信号互相干扰，大幅提升RL训练的稳定性和最终效果

  - 长路径交互场景可采用迭代全局摘要作为唯一持久状态，替代全量历史上下文，既降低KV cache占用、避免上下文溢出，还能过滤历史噪音，减少冗余搜索/召回

  - 若使用闭源大模型搭建深度搜索/导购能力，直接套用IterSynth的Prompt流程即可获得稳定增益，实测在主流闭源/开源大模型上相对ReAct有4%~10%的效果提升，可快速落地验证'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有ReAct风格深度搜索Agent存在两大核心瓶颈：一是角色耦合，单策略需同时处理规划、证据筛选、答案合成等异构任务，易出现冗余搜索、提前终止等问题；二是上下文累积，不断增长的搜索历史会引入大量噪音，超过64K上下文的ReAct在BrowseComp基准上有59%的案例因上下文溢出提前终止。多Agent方案虽能解耦角色，但会提升部署成本与协作开销，传统摘要方案则将摘要作为外部模块，无法与搜索策略联合优化。

### 方法关键点
- 架构：单LLM共享参数，仅通过角色Prompt、动作约束实现Planner与Synthesizer双角色解耦，交替执行：Planner仅基于原始问题+当前全局摘要判断是否继续搜索/输出答案；Synthesizer仅基于新召回证据更新全局摘要，摘要作为唯一持久状态，每轮重建上下文，避免累积膨胀
- 训练：冷启动阶段用大模型生成10K条高质量双角色搜索轨迹，过滤得到87.4K角色-conditioned样本做SFT；RL阶段提出RDPO算法，结合终端正确性奖励与轮次级角色专属rubric评分生成复合奖励，按角色拆分奖励池独立计算组相对优势，解决多角色信用分配混淆问题

### 关键结果
在BrowseComp、BrowseComp-ZH、GAIA、xBench-DS等5个长时序深度搜索基准上测试，IterSynth-8B平均得分50.7，比同参数规模最优基线高4.2%，中文BrowseComp-ZH上增益达15.2%，性能追平部分30B规模Agent；作为零训练Prompt范式使用时，在Claude-4.5-Opus上比ReAct平均提升5.5%，最高增益达10%。

> 最值得记住：单模型通过角色Prompt解耦能力+专属优化的收益，远高于盲目堆参数或用单一策略硬扛异构任务
