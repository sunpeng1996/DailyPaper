---
title: Recursive Harness Self-Improvement
title_zh: 递归Harness自提升（RHI）：轻量优化Agent工作流提效降本
authors:
- Hyunin Lee
- Jinglue Xu
- Jeffrey Seely
- Donghyun Lee
- Matei Zaharia
- Yujin Tang
affiliations:
- Sakana AI
- UC Berkeley
arxiv_id: '2607.15524'
url: https://arxiv.org/abs/2607.15524
pdf_url: https://arxiv.org/pdf/2607.15524
published: '2026-07-16'
collected: '2026-07-20'
category: Agent
direction: Agent工作流优化 · 轻量自迭代
tags:
- Agent
- Harness Optimization
- Self-Improvement
- Workflow Optimization
- Cost Efficiency
one_liner: 仅用数轮轻量迭代优化prompt级harness，超同模型最高推理配置效果同时降本最高60%
practical_value: '- 业务Agent调优可复用RHI的轻量迭代逻辑：不用做复杂种群搜索，每轮仅对比当前与上一版harness的输出，仅花1次Agent执行+1次LLM打分成本，适合电商客服、选品、文案生成等场景的快速定制

  - 可直接将Agent工作流抽象为prompt级harness优化，不用改底层代码，仅迭代角色分工、信息流转规则、工作流步骤，就能快速适配大促、日常运营等不同业务场景的专属需求，效果优于通用厂商内置harness

  - 优化多Agent间的信息传递契约，减少冗余上下文传递，降低KV cache读写开销，对于高并发的电商推荐文案生成、用户Query理解场景，可在提升效果的同时降低推理成本最多60%'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM Agent的性能提升依赖基础模型与harness（工作流支架）的协同进化，但厂商内置的通用harness迭代成本高、适配长尾任务效果差，传统种群搜索类的harness优化方法每轮需要多次Agent执行与评估，计算开销过高，无法满足大量业务场景下快速定制任务专属Agent工作流的需求。
### 方法关键点
- 将harness抽象为prompt级的文本规范，包含Agent角色指令、子Agent间信息传递契约、工作流控制步骤三大组件，无需修改底层代码即可迭代优化
- 采用轨迹局部松弛优化目标，每轮仅对比当前harness与上一版harness的输出，通过LLM pairwise偏好反馈指导更新，单轮迭代仅需1次Agent执行+1次评估，计算复杂度为Θ(1)
- 积累多轮偏好历史做迭代指导，降低单轮反馈噪声，仅需2-4轮即可收敛
### 关键结果
在30个跨量化金融、机器人、药学的开放式ML研究任务上测试：
- 搭配RHI的low推理配置Agent，仅需2轮迭代即可在pairwise win率上超过同模型最高推理配置（xhigh/max/ultracode）基线
- Opus 4.8搭配RHI的推理成本比ultracode基线低60%，KV cache读写开销降低64%，性能提升并非来自输出token长度增加，而是更高效的上下文管理

**最值得记住的结论**：用户自定义的prompt级任务专属harness优化效果可超过厂商内置的通用系统级harness，是低成本提升Agent性能的核心路径之一
