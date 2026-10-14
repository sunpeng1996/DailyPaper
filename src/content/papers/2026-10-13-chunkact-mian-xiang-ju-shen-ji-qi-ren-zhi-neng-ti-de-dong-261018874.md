---
title: 'ChunkAct: Action Chunking for Agentic Robotics'
title_zh: ChunkAct：面向具身机器人智能体的动作分块优化框架
authors:
- Bingxin Xu
- Wenrui Bao
- Xinxin Liu
- Jiawei Zhou
- Yuzhang Shang
- Emilio Ferrara
affiliations:
- University of Southern California
- University of Central Florida
- Stony Brook University
arxiv_id: '2610.18874'
url: https://arxiv.org/abs/2610.18874
pdf_url: https://arxiv.org/pdf/2610.18874
published: '2026-10-13'
collected: '2026-10-14'
category: Agent
direction: 具身Agent · 动作分块效率优化
tags:
- LLM Agent
- Action Chunking
- Memory Compilation
- Embodied AI
- Efficiency Optimization
one_liner: 将动作分块引入具身机器人Agent，离线编译记忆为可执行块，降LLM开销同时提成功率
practical_value: '- 做业务Agent（电商导购、售后、推荐query处理）时，可将高频固定工具调用链预编译为可执行块，无需每步调用LLM，可降低70%+的token开销和推理延迟

  - 可将RAG记忆中的固定流程（如常见咨询回复逻辑、推荐召回规则）离线编译进执行块，避免在线频繁检索，同时减少长上下文带来的推理错误

  - Agent执行失败时返回结构化错误码而非无结构日志，LLM仅处理异常场景决策，常规执行流程全自动化，大幅提升Agent稳定性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
具身机器人领域将LLM Agent纳入控制环的范式泛化性极强，无需重训即可适配新任务，但效率瓶颈突出：每个原子操作都需要LLM全量推理交互历史，输入token随步骤平方级增长，单轮简单抓取任务平均需要24.2次LLM调用、2.2M输入token，按GPT-6 Astra定价成本高达22美元/轮，且长上下文会进一步降低推理可靠性，无法规模化落地。
### 方法关键点
- 离线阶段：将记忆中同类型任务（如物品搬运、开关抽屉）的固定执行流程编译为可复用动作块，内置步骤顺序、参数规则、错误fallback、完成校验逻辑，执行时无需在线读取记忆
- 在线阶段：LLM仅承担子目标解析、异常处理两类核心决策，单次调用即可启动完整动作块，块内步骤自动链式执行，仅在失败时返回结构化错误码交回LLM重规划
- 重新定义LLM角色：从逐步执行者转为决策者，LLM计算量随决策次数而非操作步数线性增长
### 关键结果
在LIBERO-Pro benchmark上对比SOTA具身Agent方案Harness VLA：任务成功率从78.8%提升5个百分点至83.8%，LLM调用次数减少2.9×，输入token减少4.4×，输出token减少2.3×；在零样本迁移场景LIBERO-Plus上，整体成功率达83.9%，比最优VLA基线高11个百分点。
**最值得记住的结论**：LLM Agent效率优化的核心是将LLM从重复的无意义执行环节解放，仅保留真正需要推理的决策节点。
