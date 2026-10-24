---
title: 'LaLa-World: Scaling Latent World Models with Natural Language Actions'
title_zh: LaLa-World：基于自然语言动作的可扩展隐式世界模型
authors:
- Junha Song
- Geonmo Gu
- Jeongeun Park
- Heejeong Nam
- Lucas Maes
- Byeongho Heo
- Dongyoon Han
- Sangdoo Yun
affiliations:
- NAVER AI Lab
- Georgia Institute of Technology
- Brown University
- Mila & Université de Montréal
arxiv_id: '2610.27851'
url: https://arxiv.org/abs/2610.27851
pdf_url: https://arxiv.org/pdf/2610.27851
published: '2026-10-20'
collected: '2026-10-24'
category: Agent
direction: Agent 隐式世界模型规划优化
tags:
- World Model
- LLM
- Planning
- Multi-Dataset Training
- Latent Representation
one_liner: 提出基于LM的语言条件隐式世界模型LaLa-World，跨域规划性能与训练效率显著优于现有方案
practical_value: '- 做电商导购Agent/用户行为建模时，可将点击、加购、停留等数值化交互动作转成自然语言描述，解决异构跨场景行为数据的对齐难题，支持单模型联合训练

  - 做推荐系统长周期用户兴趣预判/转化路径模拟时，可复用LM底座隐式状态预测架构，无需生成完整交互序列即可做预判，推理效率高、训练成本低

  - 做电商大促流量仿真、活动效果预判类Agent规划时，可借鉴「模拟轨迹+真实多源数据联合预训练世界模型」的思路，提升规划鲁棒性，减少微调数据量'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有JEPA-style 隐式世界模型（LWM）仅支持单域单任务训练，无法融合多源异构数据，泛化性差、训练与推理成本高，难以支撑跨场景Agent规划需求。
### 方法关键点
1. 把数值动作、视觉变化统一转换为自然语言描述，打通异构数据集的训练壁垒，实现单未来预测器跨域训练
2. 基于LM搭建预测器，可同时解析语言条件、预测未来隐式状态，支持模拟/机器人轨迹、图像/视频多源数据联合训练
### 关键结果
平均MPC规划性能优于单域独立训练的现有LWM；相比RAEv2视频生成基线，同等规划性能下训练成本降低6倍，规划速度提升13.9倍；基于预训练权重初始化的LaLa-Policy在LIBERO、RoboCasa数据集上性能媲美Cosmos Policy，推理速度最高提升5.5倍。
