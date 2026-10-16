---
title: 'Cortex: Measurement-Gated Evolution and Pruning of Coding-Agent Skills and
  Rules'
title_zh: 面向编码Agent技能与规则的测量门控演化与剪枝框架Cortex
authors:
- Samuele Giampieri
affiliations:
- Independent Researcher
arxiv_id: '2610.14216'
url: https://arxiv.org/abs/2610.14216
pdf_url: https://arxiv.org/pdf/2610.14216
published: '2026-10-08'
collected: '2026-10-16'
category: Agent
direction: Agent 技能规则自动化优化
tags:
- Agent
- Prompt Optimization
- Skill Pruning
- Automatic Evaluation
- Code Agent
one_liner: 基于曝光感知与重复校验的编码Agent技能规则自动化演化、评测与剪枝工具
practical_value: '- 可直接复用「曝光感知归因」逻辑到电商导购Agent、广告文案Agent的技能库/RAG chunk效果评估：仅统计技能/Chunk实际被LLM读取/调用的会话的指标变化，排除未曝光的噪声，大幅提升归因准确率

  - 复用「多轮重复测试+分阶段校验」的方案优化业务里的prompt/技能上线流程：先小批量（k=2）跑目标场景任务筛候选，再全量（k=3）跑全场景校验，设置单case容错阈值+疑似坏case重测，抵消LLM输出随机性的影响，降低误判率

  - 参考「按适用场景自动绑定触发路径」的设计优化Agent技能加载逻辑：针对商品类目、用户意图等维度给技能绑定触发条件，做成自动加载的规则而非需要LLM主动选择的技能，既降低上下文token消耗，又避免LLM漏选技能，提升效果的确定性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent的技能、规则、系统提示等可编辑引导文本（harness）多依赖人工维护，单次验证有效就会被加入，既无系统化的效果校验，还会逐步积累无效甚至有害的内容，浪费上下文token；同时LLM输出存在天然随机性，单次测试结果不具备统计意义，传统评估也不区分技能是否实际被Agent读取/调用，准确率极低。
### 方法关键点
- 设计harvest/evolve/prune全闭环流程：harvest从开发者修正Agent的会话中自动提取带校验脚本的可复现测试任务；evolve针对重复出现的问题生成候选技能/规则，分两阶段测试（小批量主题任务筛候选，全量任务验证无负向），仅保留实际被Agent曝光且整体提效、无显著坏case的候选；prune定期校验存量技能，仅移除明确无收益的，从未被触发的技能不随意删除
- 曝光感知评估逻辑：计算技能/规则效果时，仅统计该技能实际被加载/调用的会话，排除未曝光的噪声，同时区分自动加载的rule与需要Agent主动选择的skill的触发逻辑差异
- 抗噪声校验机制：每个任务重复跑k次抵消LLM输出随机性，设置单case容错阈值，对疑似回归的任务重测避免误杀
### 关键结果
基于Claude Haiku 4.5在自定义代码仓库测试，对比无技能基线，演化出的harness在规则类任务通过率提升55pp（95% CI [34.1,74.1]），无无效内容；16/18的保留项为自动加载的rule，全局展示的skill从未被Agent调用；切换到更强的Claude Sonnet 5后，原harness增益降至5.6pp，自动剪枝掉2/4的无用技能。
**最值得记住的一句话**：对Agent技能/规则的效果评估，仅在它实际被加载到上下文的会话里计算才有意义，单次测试的结果什么都证明不了
