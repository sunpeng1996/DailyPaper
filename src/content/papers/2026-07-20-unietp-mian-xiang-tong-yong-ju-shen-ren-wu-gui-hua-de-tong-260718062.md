---
title: 'UniETP: Unifying Environments for Generalizable Embodied Task Planning'
title_zh: UniETP：面向通用具身任务规划的统一环境与评测基准
authors:
- Peiran Xu
- Jiaqi Zheng
- Ziyou Wang
- Yadong Mu
affiliations:
- Peking University
arxiv_id: '2607.18062'
url: https://arxiv.org/abs/2607.18062
pdf_url: https://arxiv.org/pdf/2607.18062
published: '2026-07-20'
collected: '2026-07-21'
category: Agent
direction: 具身Agent · 统一环境与任务基准
tags:
- Embodied Agent
- Task Planning
- Benchmark
- Unified Interface
- VLM Evaluation
one_liner: 统一4款主流具身模拟器，搭建多难度、多维度的具身Agent任务规划评测体系
practical_value: '- 做跨场景Agent开发时，可借鉴分层统一接口设计，将不同业务场景（如电商多垂类导购、客服）的观测、动作空间标准化，大幅降低Agent跨场景迁移的适配成本

  - 做Agent能力评测时，可复用其M1/M2/M3多难度档位+5维能力拆分（原子/组合/逻辑/语言/Instance Grounding）的设计，细粒度定位业务Agent的性能短板

  - 做Agent训练数据生产时，可参考「模板+常识库+LLM自动生成+可行性校验」的 pipeline，低成本生成大量符合业务逻辑的多难度SFT样本

  - 做交互Agent反馈机制设计时，优先给Agent提供二元成功/失败信号，投入ROI显著高于复杂的失败原因解释文本'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有具身任务规划的模拟器彼此孤立，观测格式、动作定义、评测标准互不兼容，导致Agent难以跨环境迁移，训练数据的规模和多样性受限，也无法系统性评测VLM的具身规划能力。

### 方法关键点
- 环境层统一4款主流具身模拟器（AI2-THOR、VirtualHome、Habitat、BEHAVIOR），定义标准化多粒度观测空间、动作空间，以统一场景图作为环境抽象，实现跨模拟器的一致评测逻辑
- 设计3档难度评测模式M1/M2/M3，通过控制场景先验信息开放程度、动作粒度，模拟从全知场景到完全未知探索的不同应用场景
- 任务层基于138个人工定义模板，结合常识库、LLM自动生成多维度任务，覆盖原子/组合/逻辑/语言/Instance Grounding 5类能力维度，产出536条评测任务、9k条训练任务

### 关键实验
评测20+主流VLM（闭源如GPT-5.5、Gemini系列，开源如Qwen、InternVL、具身专用模型），核心结果：
1. M1模式下闭源模型平均准确率最高76%，M2模式下骤降到35%，M3模式下原子任务准确率最高仅40%
2. Instance Grounding是最大性能瓶颈，即使最强闭源模型在该维度准确率仅50%左右
3. 用UniETP生成的数据做SFT，Qwen3.5-4B性能超过27B级别的基线模型，且具备跨模拟器/跨任务类型的泛化能力

### 核心结论
当前VLM的具身规划性能瓶颈主要来自实例级感知定位、未知环境探索能力，而非逻辑或语言理解，统一标准化的环境接口可大幅提升Agent的泛化训练效率
