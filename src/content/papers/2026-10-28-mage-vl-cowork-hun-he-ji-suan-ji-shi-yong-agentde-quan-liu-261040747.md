---
title: 'Mage-VL-Cowork: A Full Training Recipe to Learn Hybrid Computer Use From Evolved
  Harnesses'
title_zh: Mage-VL-Cowork：混合计算机使用Agent的全流程训练方案
authors:
- Xiaoyi Zhang
- Haoqing Wang
- Xinjie Zhang
- Xiang Ming
- Xing Wang
- Senqiao Yang
- Kaichen Zhang
- Zhaoyang Jia
- Andong Tan
- Xinjiang Wang
affiliations:
- Microsoft
arxiv_id: '2610.40747'
url: https://arxiv.org/abs/2610.40747
pdf_url: https://arxiv.org/pdf/2610.40747
published: '2026-10-28'
collected: '2026-11-04'
category: Agent
direction: 端侧智能 · 混合计算机使用Agent
tags:
- Computer Use Agent
- Multimodal Agent
- Reinforcement Learning
- SFT
- On-device Intelligence
one_liner: 4B参数量混合GUI与终端操作的计算机使用Agent，OSWorld-Verified得分达66%
practical_value: '- 训练多工具调用Agent时，可参考先演化teacher harness（剪枝冗余工具、优化prompt/工具接口）再生成训练数据的思路，避免把教师的不优路由习惯传递给学生，小模型效果提升更明显

  - 多能力Agent训练可复用5阶段渐进式课程：先分别训练单技能（GUI交互、代码终端）再做混合SFT+RL，相比直接混合训练收敛更快、小模型效果更好

  - 生成大规模训练任务时，可参考workflow-first模式：针对每个原子技能构建可复用的生成工作流+应用预处理器，能降低80%+的单任务生成成本

  - 做Agent效果评估时，可参考WebVoyager-Static的设计：不仅看最终输出，还要校验操作轨迹、后端状态，避免VLM单判导致的分数虚高'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有计算机使用Agent要么仅支持GUI交互，操作步骤多、token成本高；要么简单拼接GUI与工具调用模块，存在通道选择混乱、效果差的问题，且大参数量模型无法落地端侧，同时传统逐任务生成训练数据的模式成本极高，无法支撑大规模训练。

### 方法关键点
- 数据层：提出Mage-CUA-Forge管线，先演化teacher harness（优化脚手架、工具接口、prompt、终端环境，剪枝冗余工具），再针对每个原子技能构建可复用的生成工作流+应用预处理器，批量生成高质量标注轨迹
- 训练层：采用5阶段渐进式课程，从通用多模态对齐checkpoint开始，依次做GUI定向预训练、GUI Agent SFT、代码终端SFT、混合CUA SFT、在线混合RL，先夯实单能力再做融合
- 工程层：自研异步RL基础设施Rollout-as-a-Service，解耦桌面环境执行、模型推理、策略优化，支撑长周期桌面任务的RL训练

### 关键结果
4B参数的Mage-VL-Cowork在OSWorld-Verified上得分66.0%，超过30B的Muse Glimmer、27B的Qwen3.6等大参数量开源模型；workflow-first任务生成模式降低82.6%的单任务生成成本、93.3%的token消耗；RL阶段相比混合SFT阶段提升10.16pp得分，同时降低25.4%的输出token。

### 核心洞见
小模型对训练数据中的通道选择歧义敏感度远高于大模型，优化teacher harness带来的学生模型收益远超过教师本身的效果提升
