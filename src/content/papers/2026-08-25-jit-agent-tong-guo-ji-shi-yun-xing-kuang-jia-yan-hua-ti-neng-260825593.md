---
title: 'JIT-Agent: Scaling Harness Intelligence via Just-in-Time Harness Evolution'
title_zh: JIT-Agent：通过即时运行框架演化提升Agent智能水平
authors:
- Guibin Zhang
- Leo Lu
- Fangzhou Xie
- Kang Zhu
- Junhao Wang
- Zhifei Xie
- Zhaochen Yu
- Zihang Liu
- Zhongxiang Sun
- Qiankun Li
affiliations:
- LV-NUS Lab
arxiv_id: '2608.25593'
url: https://arxiv.org/abs/2608.25593
pdf_url: https://arxiv.org/pdf/2608.25593
published: '2026-08-25'
collected: '2026-08-27'
category: Agent
direction: Agent 运行框架即时生成与演化
tags:
- Agent-Harness
- JIT-Synthesis
- Meta-Agent
- Policy-Optimization
- Self-Evolution
one_liner: 首个专门训练的元Agent，可为任意现成Agent大模型实时生成、修复、迭代任务适配的运行框架
practical_value: '- 可复用四模块（记忆/规划/动作/能力编排）的标准化Agent框架协议，针对电商导购、搜索Agent等不同场景快速定制harness，无需从零搭建

  - 借鉴三阶段训练思路：先基于种子案例SFT学习任务适配生成，再学习错误修复，最后用Evo-GDPO做在线迭代优化，可直接迁移到场景化Agent的框架调优

  - JIT生成的场景专属harness比通用固定harness平均降低36%API调用成本，同时提升效果，电商高并发Agent场景可直接参考该范式降本提效

  - 可借鉴流式演化机制：基于历史任务反馈动态更新harness库，推荐/导购Agent可在服务过程中持续迭代运行逻辑，无需重新训练模型'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent性能不只由基座大模型决定，运行框架（harness，含记忆管理、规划策略、工具调用逻辑等）对效果的贡献甚至超过基座，但传统harness都是人工设计、预先优化的AOT模式，无法适配异构任务需求，泛化性差，维护成本极高。

### 方法关键点
- 将Agent harness抽象为记忆、规划、动作、能力编排4个可组合模块，搭建HarnessFactory种子库，集成ReAct、Plan-and-Execute等13种主流Agent框架作为生成基底
- 三阶段训练流程：Stage I用教师蒸馏做任务适配的harness生成SFT，加偏好学习平衡效果与效率；Stage II用生成失败案例做修复训练，支持2轮内修复错误；Stage III提出Evo-GDPO策略，让模型可基于运行反馈持续迭代harness库
- 支持两种推理模式：静态生成N个候选选最优，流式推理基于历史任务反馈动态更新harness库，持续提升后续任务性能

### 关键实验
在9个Agent基准（深度搜索、规划、办公等场景）测试，对比GPT-5.6、Claude Code等基线：DeepSeek-V4-Flash加JIT-Agent后，DeepSearchQA超GPT-5.6 9.1分，OdysseyBench高4.3分；GLM-5.2最高获得20.2分提升；对比Claude Code、OpenCode等成熟固定harness，JIT生成的harness在6组对比中4组效果最优，平均降低36%API成本，所有基座模型（DeepSeek V4、Qwen3.6、Mimo-V2.5）均获得稳定效果提升。

最值得记住的一句话：Agent智能是基座模型与运行框架的共同属性，运行框架智能是独立于模型缩放的可训练、可迁移的能力维度。
