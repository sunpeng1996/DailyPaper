---
title: Self-Supervised Visual On-Policy Distillation
title_zh: 自监督视觉在策略蒸馏方法S2VOPD
authors:
- Yijiang Li
- Yijun Liang
- Yunjie Tian
- Bingyang Wang
- Ke Zhang
- Zhenfei Yin
- Di Fu
- Philip Torr
- Nuno Vasconcelos
affiliations:
- UC San Diego
- University of Maryland, College Park
- Georgia Institute of Technology
- Johns Hopkins University
- University of Oxford
arxiv_id: '2608.14144'
url: https://arxiv.org/abs/2608.14144
pdf_url: https://arxiv.org/pdf/2608.14144
published: '2026-08-13'
collected: '2026-08-17'
category: Training
direction: 多模态大模型 · 自监督在策略蒸馏
tags:
- On-Policy Distillation
- Self-Supervised Learning
- Vision-Language Model
- Knowledge Distillation
- Data Augmentation
one_liner: 通过给学生输入降质图像构建蒸馏不对称性，无标注无额外教师大幅提升多模态模型性能
practical_value: '- 电商商品理解、多模态推荐场景可直接复用不对称蒸馏思路：无需额外标注，给学生侧输入低分辨率/加噪商品图，用EMA教师的原图输出做监督，即可提升小VLM的细粒度商品识别、属性提取能力

  - 蒸馏目标优先选择α=0.5的广义JSD，相比正向/反向KL散度效果提升1%+，平衡教师信息传递和学生容错性，可直接迁移到所有多模态蒸馏任务

  - 学生侧增广选0.3~0.6倍下采样加随机高斯噪声的组合，避免裁剪等增广破坏商品主体等任务相关信息，还能降低学生侧前向计算成本，训练速度提升10%以上

  - 标注资源不足的业务场景无需额外采购标注或做大模型对齐，用该自监督蒸馏方法即可提升小VLM的感知和推理能力，小样本训练即可获得接近特权信息方法的效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有视觉在策略蒸馏（OPD）依赖教师侧的特权信息构建不对称性，要么需要更强更大的教师模型，要么需要标注答案、Ground Truth 感兴趣区域等额外监督，随着模型能力快速提升，人工标注等特权信息的获取成本越来越高，甚至无法匹配模型的能力上限，亟需无需任何特权信息的蒸馏方案。

### 方法关键点
- 反转不对称性来源：不给教师增加额外特权信息，反而给学生输入降质增广的图像，教师输入原始图像，天然构建信息差作为蒸馏信号，无需外部标注、奖励或单独训练的教师模型
- 架构设计：采用指数滑动平均（EMA）动量教师，学生基于增广图像生成on-policy轨迹，最小化教师基于原图的输出分布和学生基于增广图的输出分布的广义JSD散度做优化，训练更稳定
- 增广策略选择：系统探索信息缩减、几何、光度、遮挡四类增广空间，验证最优增广为0.3~0.6倍下采样加概率0.5的高斯噪声，保证信息差足够且不破坏任务相关信息

### 关键实验
在6个细粒度视觉感知基准、3个数学推理基准上测试：基于Qwen3.5-4B底座，S2VOPD将平均感知准确率从70.7%提升至77.4%，超过235B参数的Qwen3-VL-Instruct和GPT-5.4，性能匹配397B的Qwen3.5；相同训练数据下，恢复了特权信息方法96%的性能提升，同时兼顾感知（+6.7%）和数学推理（+3.7%）能力提升，避免了特权信息方法损伤推理能力的问题。

### 核心结论
在策略蒸馏的有效不对称性不一定来自教师的信息增量，也可以来自学生侧的信息减法，零成本即可生成高质量监督信号。
