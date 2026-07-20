---
title: 'SkillCorpus: Consolidating and Evaluating the Open Skill Ecosystem for Real-World
  LLM Agents'
title_zh: SkillCorpus：面向真实场景LLM Agent的开源技能生态整合与评估框架
authors:
- Yanze Wang
- Pengfei Yao
- Tianyi Sun
- Chuanrui Hu
- Yan Xiao
- Yunyun Han
- Jun Sun
- Yafeng Deng
affiliations:
- EverMind
- Shanda Group
- Peking University
arxiv_id: '2607.15557'
url: https://arxiv.org/abs/2607.15557
pdf_url: https://arxiv.org/pdf/2607.15557
published: '2026-07-17'
collected: '2026-07-20'
category: Agent
direction: LLM Agent · 开源技能库建设与评估
tags:
- SkillCorpus
- Agent Skill
- LLM Agent
- Retrieval System
- Skill Evaluation
one_liner: 从82万开源SKILL.md中筛选出9.6万可商用高质量技能，搭配检索栈稳定提升LLM Agent任务表现
practical_value: '- 搭建内部Agent技能库可直接复用6级清洗流水线：结构校验→两级去重（精确指纹+语义余弦≥0.995自动合并，0.9-0.995由LLM判定）→三质量维度打分→硬安全门过滤→OSI许可校验→分类打标，快速落地合规高质量技能库

  - 技能检索栈可直接复用架构：微调领域embedding召回→微调重排模型→LLM全量读取技能内容做最终选择，仅返回0-2个相关技能，平衡准确率和上下文开销，适配电商客服、运营Agent的工具调用场景

  - 技能迭代优先级参考：增益与技能覆盖度强相关，高匹配分任务增益可达25.1pp，低覆盖领域增益趋近于0无负向，优先补高需求领域技能比优化检索收益更高'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前开源SKILL.md技能生态碎片化、冗余、质量参差不齐，无统一商用合规的高质量技能库，且未筛选的社区技能库常出现不如无技能基线的问题，社区技能对真实Agent任务的增益边界也未被系统性验证。

### 方法关键点
- 聚合62个渠道的82.1万份原始SKILL.md文件，经过6级流水线清洗：结构校验→两级去重→LLM judge从utility/robustness/safety三个维度打分→19个质量/安全标签校验（5个硬安全门直接过滤风险技能）→OSI开源许可校验→附加16类分类标签、预计算1024维embedding，最终得到96401份可商用高质量技能。
- 配套微调的检索选择栈：微调Qwen3-Emb-0.6B做召回，微调Qwen3-Rank-0.6B做重排，最后加LLM选择器读取全量技能内容，返回0-2个最相关技能注入prompt，可选加query rewrite适配技能词汇。

### 关键结果
跨3个基准（SkillsBench、GDPVal、QwenClawBench）、2个Agent框架、2个开源基座测试，相比无技能基线均有稳定增益：SkillsBench平均+7.5pp（最高+13.4pp），GDPVal平均+1.51pp，QwenClawBench平均+2.79pp，Claude Opus 4.7上同样获得+8.0pp增益；消融实验显示高质量语料和微调检索栈各贡献约一半增益，单独使用原始语料或通用检索栈增益仅为全链路的40%左右。

**最值得记住的一句话**：高质量合规的社区技能库是Agent能力的可靠增量，增益上限由技能覆盖度决定，下限由Agent框架的执行编排能力决定。
