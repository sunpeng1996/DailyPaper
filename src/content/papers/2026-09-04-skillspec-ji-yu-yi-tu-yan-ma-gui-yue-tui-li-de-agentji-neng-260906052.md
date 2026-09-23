---
title: 'SkillSpec: Intent-Masked Specification Reasoning for Agent Skill Correctness'
title_zh: SkillSpec：基于意图掩码规约推理的Agent技能正确性检测
authors:
- Yizhuo Zhang
- Bo Kang
- Yi Yang
- Zhiyu Duan
- Zhouteng Ye
- Shunkun Yang
affiliations:
- 北京航空航天大学
arxiv_id: '2609.06052'
url: https://arxiv.org/abs/2609.06052
pdf_url: https://arxiv.org/pdf/2609.06052
published: '2026-09-04'
collected: '2026-09-23'
category: Agent
direction: Agent技能自动化质量保障
tags:
- LLM Agent
- Skill Validation
- Specification Reasoning
- Intent Mask
- Hoare Logic
one_liner: 提出多视图意图掩码的Hoare风格框架，自动检测Agent技能意图与实现的语义不一致缺陷
practical_value: '- 若业务维护Agent技能库（如电商客服应答、推荐策略执行、广告投放流程技能），可直接复用这套ExpectSpec/FactSpec的Hoare风格对比框架，检测技能描述与实现的语义不一致问题，避免被大模型能力掩盖的静默故障

  - 做语义一致性校验时可借鉴多视图意图掩码设计：给检测对象暴露不同粒度的上下文（仅自身/链路/全局）分别抽取事实特征，再联合推理，可降低全量上下文带来的推理偏差，提升检测精度6%以上

  - 工程上可复用异构资源统一建模思路：将技能的自然语言描述、多语言脚本、配置文件绑定为双向关联的图结构，既提升缺陷检测精度，也方便后续的缺陷溯源定位

  - 纯文本无代码的流程类技能缺陷检测精度比代码类低12个百分点，落地时建议优先覆盖带可执行代码的核心技能，ROI更高'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent生态中技能复用度快速提升，半年内已发布超20万款可复用技能，但现有质量检测仅关注传统代码缺陷，忽略了自然语言声明的意图与实际实现的语义不一致问题（如描述承诺不修改源文件、实际代码会删除输入资源），这类缺陷会被大模型自身能力掩盖为静默故障，难以通过常规运行时错误排查。
### 方法关键点
1. 异构资源统一建模：将技能的Markdown描述解析为工作流DAG，将多语言代码转换为语言无关的中间表示并构建调用图，通过双向绑定关联意图节点与实现节点；
2. 意图掩码多视图规约抽取：设计4层上下文可见度（自身/邻居/链路/全局），为每个节点抽取全量意图下的预期规约ExpectSpec，以及不同掩码下的事实规约FactSpec，平衡上下文过多导致的推理偏差和过少导致的误判；
3. 联合推理+沙箱验证：对比两类规约的不一致得到候选缺陷，再通过隔离沙箱执行代码探针或场景复现，过滤误报并留存验证证据。
### 关键实验
在515个真实世界技能（来自SkillsBench与高下载量公开技能库）上测试，共识别出239个技能的763个人工确认缺陷，整体检测精度61.2%，其中代码类缺陷精度67.1%，工作流类缺陷精度55.4%，跨GPT、DeepSeek、Qwen多个模型家族均稳定有效。
### 核心结论
91.6%的代码缺陷、74%的工作流缺陷均来自声明意图到实现的语义不一致，而非纯语法bug，Agent技能质量保障必须覆盖跨语义层的一致性校验，不能仅依赖传统代码测试。
