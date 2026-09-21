---
title: 'MintAct: A Unified Visual Agent for Digital Environments'
title_zh: MintAct：面向数字环境的统一视觉智能体
authors:
- Mingfei Gao
- Rui Tian
- Haiming Gang
- Bohan Zhai
- Le Zhang
- Yuanzheng Gong
- Di Feng
- Ege Özsoy
- Kaixin Ma
- Vishwesh Kirthivasan
affiliations:
- Apple
arxiv_id: '2609.22083'
url: https://arxiv.org/abs/2609.22083
pdf_url: https://arxiv.org/pdf/2609.22083
published: '2026-09-17'
collected: '2026-09-21'
category: Agent
direction: 多模态视觉Agent 跨数字环境统一
tags:
- Visual Agent
- UI Grounding
- Asynchronous RL
- Multimodal LLM
- Tool Use
one_liner: 苹果推出2B/4B/8B参数跨移动/桌面/网页/工具调用的统一视觉Agent，性能优于同规模单域专家
practical_value: '- 跨域Agent训练可复用「单域RL专家蒸馏+统一模型联合RL」的流程，避免多模型维护成本，适合电商APP/网页/桌面端多场景运营Agent的统一开发

  - 异步RL框架的「跨域配额控制+背压机制」可直接迁移至多场景推荐/广告的联合RL训练，解决不同场景数据产出速度不均导致的训练分布漂移问题

  - 多阶段SFT的设计（高分辨率单步接地+低分辨率多步交互）可复用在电商导购Agent的UI交互能力训练中，平衡定位精度和长交互序列的训练效率

  - 动态工具注册的轨迹分割方法可直接用于电商工具调用类Agent的SFT数据构造，解决工具动态加载带来的系统prompt变化问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有视觉Agent多为单域专家，仅支持移动端/桌面/网页/工具调用单一能力，多模型部署维护成本高，不适合端侧落地；直接混合多域数据训练会出现域干扰导致单域性能下降，且多域RL训练存在环境延迟不均、训练分布漂移、长多模态轨迹内存开销大等痛点。

### 方法关键点
- 统一设计：支持2B/4B/8B三档参数，所有域统一基于原始截图的归一化像素坐标作为接地空间，通过域专属系统prompt引导模型输出对应动作集，训练全程保持四域数据均衡配比
- 多阶段训练：高分辨率单步SFT学习UI接地能力→低分辨率多步SFT学习跨域长交互能力→训练单域RL专家后通过RFT（拒绝采样蒸馏）合并能力到统一模型→异步RL联合优化跨域表现
- 异步RL框架：解耦rollout与训练流程，引入跨域配额控制+背压机制保证训练分布稳定，通过多模态数据落盘降低长轨迹内存开销，双裁剪PPO目标+截断重要性权重解决off-policy漂移和训练/推理引擎数值差异问题

### 关键结果
在OSWorld-Verified、AndroidWorld、Online-Mind2Web等7个主流跨域Agent基准测试，对比同规模单域专家模型；MintAct-8B在OSWorld-Verified达48.9（SOTA）、AndroidWorld达67.0、Online-Mind2Web达39.1，性能均优于同规模单域专家，较初始化的Qwen3-VL-8B平均提升超40%。

**核心结论**：统一多域视觉Agent不需要以牺牲单域性能为代价，通过合理的训练流程、分布控制和RL框架设计即可实现跨域能力统一与单域性能的兼顾。
