---
title: 'PoTRE: Test-Time Reasoning inspired by Cognitive Heterogeneity'
title_zh: 受认知异质性启发的多拓扑推理集成框架PoTRE
authors:
- Anmol Kankariya
- Sercan Ö. Arık
affiliations:
- Google Cloud Applied AI
arxiv_id: '2607.20268'
url: https://arxiv.org/abs/2607.20268
pdf_url: https://arxiv.org/pdf/2607.20268
published: '2026-07-22'
collected: '2026-07-23'
category: MultiAgent
direction: 多智体推理 · 测试时优化
tags:
- Multi-Agent
- Test-Time Reasoning
- LLM Reasoning
- Heterogeneous Ensemble
- Task-Adaptive Aggregation
one_liner: 构建4种差异化推理拓扑的多Agent框架，搭配任务自适应聚合，实现低推理成本下的SOTA推理性能
practical_value: '- 推理类Agent（如电商客服咨询、商品属性校验、营销文案逻辑审核）可直接复用4种差异化Agent设计：对抗校验+分层规划+多候选搜索+直接推理，覆盖不同推理失败场景，避免单一prompt的模式崩溃

  - 多Agent聚合层可借鉴任务自适应策略：约束类任务（如满减规则计算、库存校验）用候选选择，开放类（如文案生成）用语义融合，规则类（如活动准入判定）用神经符号验证，准确率比简单多数投票高20%+

  - 小模型效果提升可复用「scaffolding lift」思路：无需盲目升级大模型，给小模型加异构多Agent推理脚手架，即可在专业领域（如电商合规审核、金融风控）超过更大参数的单模型基线，推理成本最高降85%

  - 高难度任务（如复杂用户query解析、跨场景推荐规则推导）可优先触发Spectrum Search Agent做广度探索，它能解决14%其他所有Agent都无法处理的边界case，补充覆盖能力'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM测试时推理方案（CoT、自一致性、思维树等）多采用同质推理拓扑，错误高度相关，极易出现拓扑模式崩溃，在长程规划、新抽象推理、强约束场景下性能极差；单纯通过扩模型参数、增加采样次数提升效果的性价比极低。

### 方法关键点
- 异构多Agent并行架构：设计4种完全差异化推理拓扑的Agent，分别对应LLM典型推理短板：对抗精炼Agent（解决幻觉、逻辑校验问题）、分层战略规划Agent（解决长任务拆解、全局规划问题）、频谱搜索Agent（解决局部最优、探索不足问题）、直接链式Agent（作为基础CoT锚点）
- 任务自适应聚合层：根据任务类型匹配最优聚合策略：约束类任务（选择类、短答案）做候选择优，开放类任务（长文本、专业判断）做语义融合，规则类任务（逻辑推导、符号计算）做神经符号校验，规避简单多数投票的群体思维问题
- 模块化可裁剪：支持根据业务场景裁剪冗余Agent，最高可减少85%token消耗，部分场景下甚至可提升准确率

### 关键结果
- 三个基准测试达SOTA：HLE（人类终极考试）准确率49.92%，超越此前官方最优成绩；ARC-AGI-2准确率38.3%，接近基线的2倍；PRBench金融困难集平均截断分0.5196，刷新SOTA
- 小模型增益显著：Gemini-3-Flash搭配PoTRE后，推理效果超过单跑的Gemini-3-Pro基线，异构拓扑方案在绝大多数场景下优于16采样的自一致性基线
- 少数派答案恢复能力突出：当正确答案为少数派（多数投票准确率为0）时，聚合层可恢复22%~41%的正确答案，带来2%+的绝对准确率提升

> 最值得记住的一句话：将测试时算力合理分配到差异化推理拓扑，性价比远高于单纯堆模型参数或同质采样，甚至可实现小模型推理效果超过大模型。
