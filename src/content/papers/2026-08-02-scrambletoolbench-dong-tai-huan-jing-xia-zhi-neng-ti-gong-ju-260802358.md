---
title: 'ScrambleToolBench: Agents Search Exhaustively Even When Their Own Map Points
  to the Next Step'
title_zh: ScrambleToolBench：动态环境下智能体工具行为推理评测基准
authors:
- Vernon Toh
- Navonil Majumder
- Zhengyuan Liu
- Nancy F. Chen
- Soujanya Poria
affiliations:
- Nanyang Technological University, Singapore
- Agency for Science, Technology and Research (A*STAR), Singapore
arxiv_id: '2608.02358'
url: https://arxiv.org/abs/2608.02358
pdf_url: https://arxiv.org/pdf/2608.02358
published: '2026-08-02'
collected: '2026-08-04'
category: Agent
direction: Agent工具使用 · 动态环境推理评测
tags:
- Agent
- Tool-Use
- Benchmark
- Reasoning
- Dynamic Environment
one_liner: 提出无语义提示、含动态漂移的工具交互评测基准，暴露现有Agent的行为推理缺陷
practical_value: '- 做电商/广告内部Agent工具调用系统时，可参考工具ID混淆方案测试Agent不依赖语义先验的推理能力，避免API语义变动或文档过时导致的故障

  - 动态环境下的Agent可采用双库持久化记忆架构（任务配方库+工具知识库），搭配定期内存剪枝策略，降低API漂移、网络抖动场景下的重复探索成本，减少信念惯性

  - 针对业务中API版本迭代、接口映射变更场景，可复用Cycle Tracing算法，仅需少量额外调用即可快速恢复工具映射，避免暴力搜索带来的token和耗时损耗

  - 优化Agent推理路径时不要盲目堆叠推理步数，高推理开销往往仅提升暴力搜索覆盖率，不会自动触发更高效的演绎推理策略，需针对性设计规则引导'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有工具使用评测基准均提供静态、语义明确的工具schema，Agent依赖预训练语义先验即可完成任务，无法评测无文档、环境动态变化（API漂移、随机故障、执行时限）场景下的行为推理能力；而实际生产环境中API文档过时、功能变更、网络抖动是常态，亟需能隔离纯行为推理能力的评测基准。

### 方法关键点
- 全维度工具语义混淆：函数名、参数名、输出字段、执行状态全部随机化，仅保留提交任务等元命令语义，强制Agent通过试错发现工具行为
- 连续任务课程设计：单episode包含5个关联任务，工具知识可跨任务复用，测试知识沉淀与复用能力
- 三类动态环境挑战：映射漂移（部分工具ID随机重分配）、随机执行失败（模拟网络超时）、temporal执行窗口（触发后需在k步内完成任务）
- 记忆增强基线：双库结构化记忆（任务配方库存通用步骤、工具知识库存工具映射与置信度），支持动态更新与剪枝

### 关键结果
评测15款开源+闭源SOTA模型，无混淆环境下平均episode完成率93%，加入所有动态挑战后骤降至3%；增加持久记忆可平均提升完成率9pct、平均多完成0.59个任务；现有模型基本不会主动采用Cycle Tracing高效恢复策略，高推理步数仅提升暴力搜索强度，token开销提升3.5~4.6倍但不带来推理策略优化。

### 核心结论
现有LLM Agent的工具使用能力严重依赖语义先验，面对环境变化时普遍存在信念惯性，仅靠增加记忆或推理步数无法自动获得高效的演绎推理能力
