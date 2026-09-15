---
title: 'ReactHuman: A Physics-Grounded Benchmark for Human-Like Reactive Decision-Making
  in Embodied Multimodal LLMs'
title_zh: ReactHuman：面向具身多模态大模型类人反应决策的物理基准
authors:
- Yizhan Li
- Jianxin You
- Mengyang Xiong
- Yinhuan Chen
- Zicheng Zhao
- Dekun Wu
- Dongqing Zhang
- Bang Liu
affiliations:
- Université de Montréal
- Mila – Quebec AI Institute
- McGill University
- McMaster University
- Meta Platforms
arxiv_id: '2609.10895'
url: https://arxiv.org/abs/2609.10895
pdf_url: https://arxiv.org/pdf/2609.10895
published: '2026-09-08'
collected: '2026-09-15'
category: Agent
direction: 具身Agent · 多模态大模型决策评估
tags:
- Embodied Agent
- Multimodal LLM
- Benchmark
- Physics Grounding
- Safety Decision
one_liner: 首个基于物理仿真的具身MLLM突发安全场景反应决策基准，覆盖千余可复现家庭危险场景
practical_value: '- 做服务类具身Agent（如电商线下配送/门店导购机器人）的团队，可复用该基准的「物理真实场景+对抗样本」设计思路，补充安全决策模块的测试用例

  - 开发Agent实时决策系统时，可参考其「合理性/安全性/物理一致性」三维评估指标体系，优化决策结果的校验逻辑

  - 业务落地不要盲目堆大模型参数：该研究证实参数规模提升无法解决物理场景反应决策失效问题，需额外引入轻量物理规则模块做兜底'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有具身MLLM评估多为被动视频问答或长程规划任务，无法验证模型是否能将物理常识转化为即时安全决策，是家用/服务类具身Agent落地的核心卡点。
### 方法关键点
1. 构建ReactHuman基准：覆盖17类家庭突发危险事件、1000+可复现仿真场景，ground truth来自240Hz刚体仿真，包含外观与物理属性矛盾的对抗样本（如泡沫铁砧、钢制苹果）
2. 设计5项评估指标，从合理性、安全性、物理一致性三维度打分，所有决策直接在仿真中执行以观测实际后果
### 关键结果数字
测试7款主流MLLM，平均每3个危险场景就有1个处理错误；失效模式包括依赖固定经验而非场景观测、信任外观胜过运动规律、动作逻辑正确仍错过米级拦截点，且这类失效不会随模型规模扩大而减少。
