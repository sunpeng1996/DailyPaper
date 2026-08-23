---
title: 'VTInstructor: Visual Trajectory Prompting for Navigation Instruction Generation
  in Continuous Environments'
title_zh: VTInstructor：面向连续环境导航指令生成的视觉轨迹提示框架
authors:
- Haolin Yang
- Yuxing Long
- Zihan Yang
- Hao Dong
affiliations:
- Peking University
- PrimeBot
arxiv_id: '2608.15284'
url: https://arxiv.org/abs/2608.15284
pdf_url: https://arxiv.org/pdf/2608.15284
published: '2026-08-15'
collected: '2026-08-23'
category: Multimodal
direction: 多模态视觉语言 · 导航指令生成
tags:
- Visual-Language Navigation
- Instruction Generation
- Visual Prompting
- Trajectory Modeling
- Multimodal Generation
one_liner: 首个无需导航图与3D重建的连续环境VLN指令生成框架，多指标达SOTA且可增强下游导航数据
practical_value: '- 轨迹类多模态任务（如用户逛店行为理解、AR导购路径规划）可复用EDTC关键帧蒸馏逻辑，降低长序列输入的计算开销

  - 隐式空间信号可通过VTP叠加路径/目标提示的方式转为显式视觉提示，无需额外3D建模即可增强多模态编码器空间感知能力

  - 生成式指令类任务可借鉴VT-GRPO训练校准方法，提升生成内容的下游任务实用性，而非仅优化NLG自动指标'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有VLN导航指令生成方案依赖离散视角图与全景观测，仅适配结构化场景；连续环境下智能体仅能获取密集RGB流，轨迹结构隐式难以提取，无法生成高可用导航指令。
### 方法关键点
无需导航图、预构建地图或场景重建：1）EDTC模块将长RGB轨迹蒸馏为导航关键帧；2）VTP模块将路径、转向、目标提示叠加到关键帧，将隐式轨迹几何转为显式视觉提示；3）VTMod模块将轨迹信号注入视觉编码器；4）训练阶段采用VT-GRPO校准空间注入过程。
### 关键结果
在R2R-CE、RxR-CE Val Unseen基准上所有NLG指标达SOTA，较最优基线分别提升0.357、0.109 CIDEr；生成的指令将冻结导航跟随者成功率提升至63.3%，较最优竞品高14.7个百分点；用于下游导航任务数据增可带来3个百分点的SR提升。
