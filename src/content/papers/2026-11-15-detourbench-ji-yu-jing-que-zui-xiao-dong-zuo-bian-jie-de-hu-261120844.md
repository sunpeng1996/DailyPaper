---
title: 'DetourBench: Trajectory-Level Evaluation of Interactive Agents with Exact
  Minimum-Action Bounds'
title_zh: DetourBench：基于精确最小动作边界的交互Agent轨迹级评估基准
authors:
- Hanlin Tian
- Sihan Zhu
- Zhao Yang
- Yuxiang Wang
- Zhiquan Hu
- Yu Mi
- Hongquan Zhu
- Qiufei Hu
affiliations:
- Datagrids.ai
- Northwestern Polytechnical University
- Nanyang Technological University
- East China Normal University
- Peking University
arxiv_id: '2611.20844'
url: https://arxiv.org/abs/2611.20844
pdf_url: https://arxiv.org/pdf/2611.20844
published: '2026-11-15'
collected: '2026-11-27'
category: Eval
direction: Agent 轨迹级评估基准构建
tags:
- Agent Evaluation
- Trajectory Measurement
- Benchmark
- LLM Agent
- Interactive System
one_liner: 提出带精确最小动作边界的交互Agent轨迹评估基准，可区分不同质量的成功与失败轨迹
practical_value: '- 电商导购Agent、多轮商品咨询Agent的效果评估可复用该框架的轨迹成本计算逻辑，不只看最终成交/查询成功率，还可统计多余交互次数、近成功失败占比，精准定位Agent规划冗余点

  - 评估多轮交互类推荐（如定制化穿搭推荐、售后问题解决方案推荐）时，可通过穷举最短交互路径作为基准，量化不同模型的交互效率，筛选出步骤更少、用户摩擦更低的Agent方案

  - 可复用其有限状态转移系统、剩余工作量计算方法，构建内部Agent测试集，自动区分可恢复的near miss失败、不可逆错误、无效重复调用三类故障，针对性迭代Agent的规划和工具调用逻辑'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有交互Agent评估仅以最终任务完成度为核心指标，无法区分高效直达、冗余探索两类成功轨迹，也无法区分差1步完成的近失败、完全偏离目标的低效失败、不可逆错误三类失败场景；人工标注的参考路径无法证明是最短最优，缺少客观的效率评估基准，难以量化Agent交互过程的优劣。

### 方法关键点
- 将每个任务抽象为有限部分可观测转移系统，资源发现后可直接访问无回溯成本，单步动作成本统一，通过BFS穷举计算全信息下完成任务的最小动作数Lo，同时生成可复现的最短路径见证
- 对未完成的可恢复轨迹计算精确剩余工作量RT，不可逆错误单独标记无有限RT；设计4类互补指标：成功率、条件达成率（Lo/成功轨迹动作数，越高越高效）、剩余进度、归一化绕路率
- 构建两类任务集：控制变量机制集（仅修改提示中的线索句，其余变量固定）、集成工作流集（覆盖金融、物流、医疗等25个复杂多步任务），所有任务带哈希校验、可复现验证

### 关键结果
在25个集成任务上测试5个主流LLM Agent端点，共375次测试：成功率范围58.7%~96.0%，条件达成率范围0.803~0.890，二者排序不完全一致（如GLM成功率最低但条件达成率高于DeepSeek和Qwen）；8个所有模型全成功的任务，模型间条件达成率差异可达0.19，可区分纯效率差距；99次失败中可分解为2次不可逆错误、47次差2步内的近失败、其余低效探索失败。

### 核心结论
交互Agent的评估不能只看最终结果，效率和失败模态的差异对落地体验的影响远大于二进制的成功/失败标签。
