---
title: 'Coda-DaVinci: Reimagining Video Generation with Code2Video'
title_zh: Coda-DaVinci：基于Code2Video的视频生成范式重构
authors:
- Yiyan Ji
- Qixun Wang
- Yang Shi
- Zhuoran Zhang
- Yifan Xu
- Tengfei Liu
- Yuqi Tang
- Xiaohan Zhang
- Shujie Li
- Jiafu Tang
affiliations:
- Nanjing University
- KlingAI Research
- Peking University
- Hong Kong University of Science and Technology (Guangzhou)
- University of Hong Kong
arxiv_id: '2611.26595'
url: https://arxiv.org/abs/2611.26595
pdf_url: https://arxiv.org/pdf/2611.26595
published: '2026-11-18'
collected: '2026-11-20'
category: MultiAgent
direction: 多智体协作 · 可控视频生成
tags:
- Code2Video
- Multi-Agent
- 3D Proxy
- Video Generation
- Prompt Alignment
one_liner: 提出任务自适应多智体Code2Video框架，通过3D代理粒度适配提升视频生成质量与可控性
practical_value: '- 多模态生成场景可复用「任务路由+粒度自适应」的智体调度逻辑，根据任务类型切换直接生成/代理引导生成路径，平衡生成质量与可控性

  - 跨模态引导生成场景可借鉴「代理对齐提示工程」方法，将3D结构、物理模拟等结构化先验绑定到prompt，降低生成内容的逻辑错误率

  - 长序列生成任务可复用多智体校验修复流程，通过独立视觉审查模块迭代修正生成结果，提升序列前后一致性'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有Code2Video范式通过Agent生成的3D代理引导视频生成，可实现结构与动态性的显式控制，但3D代理构建、提示设计的最优方案，以及该范式的能力边界尚未被充分探索。
### 方法关键点
1. 先通过控制变量实验+盲测人类评估，明确不同策略的任务依赖trade-off：粗粒度代理适配自然动效生成，中粒度代理适配高一致性场景，物理模拟+代理对齐提示可进一步提升平均质量
2. 基于上述结论提出Coda-DaVinci多智体框架：支持任务级路由切换代理引导/直接生成路径，实体级适配3D建模粒度，绑定物理模拟结果与对应提示，搭配多智体校验管线通过视觉检查、独立评审修复生成结果
### 关键结果
VTR数据集指令遵循效果领先，R2M数据集场景一致性优于基线，物理合理性比直接生成显著提升，视觉真实度高于现有Code2Video基线；长视频生成的事件结构、多轮交互一致性明显提升，但仍存在过渡稳定性不足、场景设置贴合度有限的局限
