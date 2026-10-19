---
title: 'SimForcing: Distilling Simulation Motion Priors into Real-Domain Robot World
  Models'
title_zh: SimForcing：将仿真运动先验蒸馏到实域机器人世界模型
authors:
- Xiaodong Wang
- Tianle Li
- Chuanxin Song
- Junliang Xie
- Zhanmi Zhong
- Suiying Wu
- Peixi Peng
affiliations:
- Peking University
arxiv_id: '2610.06598'
url: https://arxiv.org/abs/2610.06598
pdf_url: https://arxiv.org/pdf/2610.06598
published: '2026-10-04'
collected: '2026-10-19'
category: Other
direction: 仿真知识蒸馏 · 机器人世界模型优化
tags:
- Knowledge Distillation
- World Model
- Simulation Priors
- Classifier-Free Guidance
- Embodied AI
one_liner: 提出SimForcing仿真引导框架，蒸馏仿真运动先验优化实域机器人世界模型性能
practical_value: '- 跨域知识蒸馏可借鉴：做不同场景（比如仿真测试流量/真实流量）的偏好/行为先验迁移时，可对齐隐空间时序变化而非表层特征，规避域间分布差异影响

  - 条件控制机制可复用：引入多块条件+dropout的方式平衡外部先验的利用与依赖，适配推荐场景中利用第三方/规则先验但避免其误差传导的需求

  - 无额外推理开销的联合训练思路：训练时引入额外监督信号，推理阶段无需额外模块，适配推荐系统低延迟要求的落地场景'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
动作条件机器人世界模型需同时精准响应机器人轨迹、保留真实视觉动态，但从异构机器人视频学习两项能力难度高；仿真虽能提供结构化运动监督，但域间外观差异阻碍直接迁移，不准确的仿真预测还会误导真实视频生成。
### 方法关键点
1. 隐空间运动蒸馏：对齐仿真教师与实域学生的隐空间时序变化，内化运动先验的同时弱化外观差异影响
2. 多块仿真条件+条件dropout：利用仿真轨迹预测的同时避免过度依赖其精度
3. 仿真条件无分类器引导，平衡内化运动先验与仿真隐空间指导的预测结果，训练后学生可同时生成仿真条件与实域视频，推理无额外模块
### 关键结果
在Bridge数据集上PSNR、SSIM、LPIPS、FVD均为对比方法最优，无需外部具身预训练；在InternData-A1数据集验证跨数据集适配性；用训练好的世界模型初始化视觉-语言-动作模型，LIBERO任务成功率显著提升
