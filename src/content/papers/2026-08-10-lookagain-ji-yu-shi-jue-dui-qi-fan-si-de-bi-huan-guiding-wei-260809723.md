---
title: 'LookAgain: Closed-Loop GUI Grounding with Visually Grounded Reflection'
title_zh: LookAgain：基于视觉对齐反思的闭环GUI定位框架
authors:
- Renshan Zhang
- Haoyang Meng
- Yixiao He
- Rui Shao
- April Hua Liu
- Liqiang Nie
affiliations:
- 哈尔滨工业大学（深圳）
- 北京邮电大学
- 深圳湾区研究院
- 上海财经大学
arxiv_id: '2608.09723'
url: https://arxiv.org/abs/2608.09723
pdf_url: https://arxiv.org/pdf/2608.09723
published: '2026-08-10'
collected: '2026-08-11'
category: Agent
direction: GUI Agent · 多轮闭环视觉定位
tags:
- GUI Grounding
- Multimodal Agent
- Closed-loop Reasoning
- GRPO
- Vision-Language
one_liner: 将GUI定位重构为预测-复盘-修正多轮闭环，在多个基准上大幅超越同规模基线
practical_value: '- 多轮自校验架构可复用在电商UI自动化Agent的元素定位场景，比如后台批量操作、直播场控机器人的按钮识别，对小尺寸、密集排布UI元素的定位增益超过10%

  - 两阶段训练范式（SFT冷启动+GRPO终局奖励优化）可迁移到所有多轮决策类Agent任务，先拿强老师模型生成的正确轨迹做SFT学交互格式，再用RL对齐终局目标，比直接RL训练收敛速度快30%以上且退化少

  - 拒识样本的CutPaste构造方法可复用在所有需要拒识能力的多模态任务，比如电商商品图审核、违禁内容识别的负样本构造，无需人工标注即可生成大量有效拒识数据

  - 小目标自动增加校验轮次的策略可用于搜索推荐的多模态召回场景，比如小尺寸商品图的语义匹配，自动触发多尺度特征校验，降低小目标漏召回率'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有GUI定位模型均为单轮预测范式，在小目标、密集布局、分布外界面场景下性能暴跌，是屏幕操作Agent级联错误的核心来源。核心缺陷是没有对已输出坐标做复盘修正：预测即终态无事后校验机制、视觉证据与预测结果解耦、迭代优化仅针对视图而非已有预测，无法复用历史预测作为空间先验。

### 方法关键点
- 范式重构：将单轮坐标回归改为多轮`predict-look-again-refine`闭环，设计两个工具原语：`locate`输出坐标假设，在原图打标记后裁剪对应区域高分辨率patch追加到上下文；`confirm`确认结果或拒识并终止流程，每轮推理都锚定上一轮预测作为空间先验。
- 两阶段训练：第一阶段用Gemini3.1-Pro生成的正确多轮反思轨迹做SFT冷启动，采用轮次选择性掩码，仅学习正确的反思和修正逻辑，不模仿错误预测；第二阶段用GRPO优化，仅以最终定位正确性作为奖励，抑制重复调用、格式错误等退化行为。
- 拒识数据构造：基于CutPaste方法篡改原图目标区域，自动生成大量目标不存在的拒识样本，搭配对应反思轨迹加入训练。

### 关键结果
在OSWorld-G、VenusBench-GD、UIVision、ScreenSpot-Pro等6个基准上测试，LookAgain-8B相比基线Qwen3-VL-8B，OSWorld-G整体准确率提升21.7个点到73.0，UIVision提升15.5个点到38.8，ScreenSpot-Pro提升13.1个点到60.2，MMBench-L2-GUI提升5.2个点到84.5；小目标场景下自动增加校验轮次，准确率增益更显著。

### 核心结论
对输出结果的视觉复盘修正，比单轮堆叠推理模块、增加感知特征的收益更高，是多模态定位任务性价比极高的优化方向。
