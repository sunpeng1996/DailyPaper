---
title: 'DyCraft: An Agentic System for Long-Horizon 4D Scene Generation'
title_zh: DyCraft：面向长时序4D场景生成的智能体系统
authors:
- Jeff Tan
- Hang Dai
- Zeqian Long
- Yanzhe Lyu
- R. Kenny Jones
- Shangzhe Wu
- Chen Geng
- Jiajun Wu
affiliations:
- Stanford University
- University of Cambridge
arxiv_id: '2610.40754'
url: https://arxiv.org/abs/2610.40754
pdf_url: https://arxiv.org/pdf/2610.40754
published: '2026-10-28'
collected: '2026-11-12'
category: Agent
direction: Agent 长时序复杂任务生成优化
tags:
- Agent
- 4D Generation
- Long-Horizon Generation
- Workflow Optimization
- Text-to-3D
one_liner: 模仿人类动画师工作流拆分长时序4D生成任务，大幅降低物理错误、提升人类偏好度
practical_value: '- 长时序复杂生成类Agent任务可借鉴「全局规划→关键帧分镜→局部补全」的拆分范式，降低单步推理复杂度，减少累积错误、提升输出一致性

  - 多步Agent工作流可引入单步独立校验机制，每完成一个子任务先做合法性校验（符合物理规则/业务规则）再进入下一步，大幅降低错误率

  - 电商3D商品展示、虚拟主播长时序动效生成场景可直接复用该工作流，减少穿模、动作不自然等问题，提升内容生成质量'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有编码Agent可生成高质量3D静态场景，但长时序动画生成频繁出现物体穿模、无物理支撑、动作不自然等物理违规问题，一次性生成全量脚本的模式难以校验输出、无法解耦复杂时空约束。
### 方法关键点
借鉴人类动画师工作流，将长时序4D生成任务拆分为三步：
1. 基于用户Prompt扩展为详细规划，先构建静态场景
2. 生成关键帧3D故事板，每个关键帧为独立静态3D场景，可单独构建、调试、校验
3. 基于已校验的起止关键帧对，调用动效工具生成局部过渡动画
### 关键结果
在24个覆盖人形机器人、人物/动物角色、物理机械的长时序多镜头动画任务上测试：相比原生GPT-6 Codex Agent及现有基线，物理违规率大幅下降，人类评估的内容偏好度显著更高。
