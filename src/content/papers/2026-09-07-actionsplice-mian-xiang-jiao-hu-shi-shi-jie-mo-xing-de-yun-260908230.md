---
title: 'ActionSplice: In-Flight Action Editing for Interactive World Models'
title_zh: ActionSplice：面向交互式世界模型的运行时动作编辑推理框架
authors:
- Pardis Taghavi
- Tingyu Guo
- Jonas Lossner
- Gaurav Pandey
- Reza Langari
affiliations:
- Texas A&M University
arxiv_id: '2609.08230'
url: https://arxiv.org/abs/2609.08230
pdf_url: https://arxiv.org/pdf/2609.08230
published: '2026-09-07'
collected: '2026-09-14'
category: Agent
direction: Agent 世界模型推理优化
tags:
- World Model
- Inference Optimization
- Interactive Agent
- Counterfactual Reasoning
- Action Editing
one_liner: 推出冻结基座的无重放运行时动作编辑推理框架，降低交互式世界模型控制延迟并提升生成质量
practical_value: '- 可借鉴CST轻量校正器思路，在生成式推荐/Agent流式输出场景中，中途插入用户实时反馈（如划走、点击、实时query）时无需重跑全链路，仅校正中间表征即可输出符合新意图的结果，降低响应延迟

  - 对于分块生成的多模态生成服务（如电商直播AI场景生成、商品详情页分块推送），可复用CST*{T}的前缀保留+后缀更新逻辑，既保留已输出的连贯内容，又快速响应用户中途的修改需求

  - 冻结基座仅新增轻量校正模块的方案可直接复用在现有已上线的生成类服务上，无需重新训练大模型，改造成本极低，适合快速迭代的业务场景'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
当前分块自回归视频世界模型每次生成1个块仅绑定1个动作，采样中途收到新动作时只能等待下一个块、沿用旧动作状态或回滚重算，无法兼顾响应速度与生成质量，控制延迟高且算力浪费严重。
### 方法关键点
推出ActionSplice推理框架，将中途动作编辑问题定义为Counterfactual State Transport (CST)，新增轻量校正器在同一步求解器阶段将被中断的基座原生表征迁移到新动作对应的匹配状态，基座模型和采样器全程冻结，无需重放已完成计算；提供两种变体：CST*{R}更新整个激活块，CST*{T}保留时间前缀仅更新后缀。
### 关键结果数字
在minWM-Wan Action2V、HY-WM1.5基准上，CST*{R}相比直接条件交换分别降低61.5%、75.9%的回滚相对LPIPS；CST*{T}分别降低56.1%、77.5%的后缀LPIPS，同时相比等待策略分别取得2.73×、1.69×的像素生成速度提升；HY-WorldPlay协议下CST*{R}的PSNR达25.66dB、SSIM达0.6902、LPIPS达0.1337。
