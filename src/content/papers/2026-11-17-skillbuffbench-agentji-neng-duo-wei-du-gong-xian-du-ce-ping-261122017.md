---
title: 'SkillBuffBench: Measuring What Agent Skills Contribute across Harnesses, Models,
  Skill Access Modes and Memory'
title_zh: SkillBuffBench：Agent技能多维度贡献度测评基准
authors:
- Gengyue Dong
- Ye Wei
- Zheng Zhu
- Yidong Han
- Jiale Miao
- Xiaojun Jia
- Guanghui Li
affiliations:
- University of Oxford
- Imperial College London
- University College London
- Nanyang Technological University
- BraneMatrix AI
arxiv_id: '2611.22017'
url: https://arxiv.org/abs/2611.22017
pdf_url: https://arxiv.org/pdf/2611.22017
published: '2026-11-17'
collected: '2026-11-18'
category: Eval
direction: Agent 技能效果测评基准
tags:
- Agent
- Benchmark
- Skill Evaluation
- LLM Agent
- Memory Effect
one_liner: 提出交叉控制技能、内存、框架、模型的Agent技能贡献度测评基准
practical_value: '- 落地Agent技能库时，不能仅评估人工投喂正确技能的上限效果，必须测试从全量技能库自动检索调用的真实表现，两者的gap直接决定业务ROI

  - 上线带记忆的Agent系统时，需做对照实验拆分记忆和技能的增益贡献，避免将记忆的效果错归为技能价值，优化时可精准定位瓶颈

  - 构建内部Agent效果评估体系时，可复用其配对bootstrap置信区间计算、passk/pass@k可靠性统计、多维度效率（成本/轮次/时间）测算的方法

  - 开发业务Agent技能时，遵循“技能仅服务一类通用问题、不得包含任务特定常量/答案”的防泄漏规范，保障技能的通用性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent技能效果测评多基于人工预先选择正确技能、无历史会话记忆的理想实验设置，与真实部署场景中Agent需从全量已安装技能库自动检索调用、可携带历史记忆的情况存在显著差异，且无法拆分模型、Agent执行框架（Harness）、技能、记忆各自的贡献，测评结果难以指导业务落地。

### 方法关键点
- 采用全因子实验设计，交叉4类变量：4种主流Agent Harness（Ginkley/Codex/Claude Code/OpenCode）、11款国内外SOTA专有/开源LLM、3种技能访问模式（无技能/人工投喂匹配技能/从技能库自动调用）、2种内存模式（关闭/开启）
- 所有任务均来自材料科学、生物学领域专家贡献的真实科研任务，每个任务配套专家日常使用的对应技能，附带确定性验证器，无LLM打分环节，结果可复现
- 统计维度覆盖：技能绝对增益Δ、归一化增益g，配对bootstrap 95%置信区间，可靠性指标passk/pass@k，以及成本、Token消耗、交互轮次、耗时等效率指标

### 关键结果
当前基准共覆盖4个领域任务，全量实验规模为11模型×4框架×3技能模式×2内存模式×4任务×3次重复=3168次运行，完整评估仍在进行中，结果将滚动更新。

### 核心结论
Agent技能的真实业务价值等于人工投喂时的上限增益减去技能检索调用失败带来的损耗，且会被记忆的增益显著抵消，脱离部署场景的技能效果测评无实际参考意义。
