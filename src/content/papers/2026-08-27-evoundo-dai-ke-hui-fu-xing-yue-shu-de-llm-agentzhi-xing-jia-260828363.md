---
title: 'EvoUndo: Recoverability-Constrained Self-Evolution for LLM Agent Harnesses'
title_zh: EvoUndo：带可恢复性约束的LLM Agent执行框架自进化方法
authors:
- Tanmay Sah
- Dolly Sah
- Harshul Jain
- Tanya Sah
affiliations:
- Independent Researcher
arxiv_id: '2608.28363'
url: https://arxiv.org/abs/2608.28363
pdf_url: https://arxiv.org/pdf/2608.28363
published: '2026-08-27'
collected: '2026-09-01'
category: Agent
direction: Agent自进化 · 可恢复性校验
tags:
- LLM Agent
- Self-Evolution
- Recoverability
- Runtime Verification
- Counterfactual Testing
one_liner: 提出可恢复性约束的LLM Agent自进化框架，解决自修改后无法跨状态安全回滚的痛点
practical_value: '- 电商/推荐场景的Agent自动迭代（如自动调优prompt、召回规则、工具调用逻辑）可复用EvoUndo的witness捕获+回滚程序+反事实校验流程，保障迭代出问题时可安全回滚，特别适合大促等稳定性要求高的场景

  - Agent自修改的错误诊断可参考结论：当恢复原语表达能力足够时，优先给粗粒度错误反馈即可，过细的状态地址信息反而可能导致大模型生成错误回滚逻辑，同时降低token消耗

  - 可直接复用两层恢复原语设计：基础的配置、prompt、工具注册修改用轻量L0原语，涉及中间件序列、资源分配的复杂修改用扩展L1原语，平衡开发成本和回滚覆盖范围'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM Agent已支持运行时修改自身prompt、工具、中间件、执行框架实现自进化，但现有方案仅优化正向效果，修改产生的持久化副作用（如覆盖配置、重排中间件、注册新监听器）无法跨状态安全回滚，一旦修改过时、出现 regression 或与后续更新冲突，静态回滚操作会失效，长期运行的电商客服、推荐策略调优类Agent会面临严重的稳定性风险。

### 方法关键点
- 每个自修改突变绑定三元组：witness捕获程序（记录修改前状态）、recovery回滚程序、效果契约（声明修改影响的状态范围），且正向突变严格不可修改，避免通过弱化功能规避回滚要求
- 反事实回环校验：生成多组IID/OOD反事实状态，验证突变在不同状态下的回滚效果，只有回滚后状态与原状态语义等价才允许上线
- 两层恢复原语设计：L0覆盖配置、prompt、工具注册等基础修改，L1扩展支持中间件序列、监听器、文件、资源等复杂结构化修改
- 两档诊断粒度：粗粒度仅返回错误子系统和类型，细粒度返回精确的状态地址和执行轨迹

### 关键实验结果
- 测试集为600个unseen单轮自进化任务，筛选出197个可提升能力但回滚失败的自然失败样本，常规修复方案在基础原语下修复成功率为0
- 细粒度地址诊断+L0原语可修复S0层（L0可覆盖）79.2%的失败；粗粒度诊断+L1原语可修复S1层（仅L1可覆盖）99.3%的失败，整体修复率达91.4%
- gpt-oss-120b上细粒度诊断+L1原语会让S1层修复率从99.3%降到93%，该负向交互效果在Qwen3.8-27B上未复现，属于模型依赖特性

### 核心结论
可靠的Agent自进化不能仅靠迭代prompt，必须协同设计校验机制、状态对齐、witness语义和恢复原语表达能力。
