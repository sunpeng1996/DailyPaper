---
title: 'Splat2Act: From Captured Scenes to Personalized VLA Manipulation'
title_zh: Splat2Act：从实景采集到个性化视觉-语言-动作操控策略
authors:
- Xiaomeng Ye
- Krishna Jaganathan
- Gyubeum Lim
- Gunjan Chhablani
- Muhammad Zubair Irshad
- Zsolt Kira
arxiv_id: '2610.13945'
url: https://arxiv.org/abs/2610.13945
pdf_url: https://arxiv.org/pdf/2610.13945
published: '2026-10-09'
collected: '2026-10-14'
category: Agent
direction: 具身Agent · VLA策略个性化
tags:
- VLA
- Embodied Agent
- Real-to-sim-to-real
- 3D Gaussian Splatting
- Policy Personalization
one_liner: 提出仅需手机扫描与物品图像的real-to-sim-to-real管线，低成本实现预训练VLA操控策略个性化
practical_value: '- 低成本个性化方案可迁移至电商线下履约/门店服务机器人场景，仅用普通手机扫描环境即可适配VLA策略，无需大量人工采集实操演示数据

  - 两阶段微调思路可复用：先在通用公开资产数据集上做域适配，再针对目标场景私域物品做小样本个性化，平衡泛化性与场景适配性

  - 仿真生成样本替代真实标注的思路可借鉴到推荐系统冷启动场景，用数字孪生生成模拟交互数据降低冷启动标注成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
通用预训练VLA策略在用户真实场景下操控成功率为0，逐场景采集真人演示数据成本过高，无法落地个性化具身操控需求。
### 方法关键点
1. 自动化real-to-sim-to-real管线仅需手持手机扫描场景+用户物品图像即可完成适配，无需额外人工标注；2. 用3D Gaussian Splatting构建建筑级室内环境数字孪生，自动识别收纳容器、生成可行抓取任务，通过仿真特权oracle生成成功演示样本；3. 两阶段微调预训练VLA：先在公开物品资产数据集上做域适配，再针对目标场景私域物品做个性化微调。
### 关键结果数字
在101个平均可通行面积104.87㎡的校园场景下，管线自动生成852个容器、超6.8万条抓取演示；个性化后VLA目标场景抓取成功率达62.5%，真实机器人Stretch 3上12项任务成功率达63.9%，与仿真结果66.7%高度吻合。
