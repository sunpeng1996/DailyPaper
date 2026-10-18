---
title: 'Dense4D: Pixel-Level 4D Human Correspondence'
title_zh: Dense4D：像素级4D人体稠密对应建模
authors:
- Rıza Alp Güler
affiliations:
- Imperial College London
arxiv_id: '2610.22325'
url: https://arxiv.org/abs/2610.22325
pdf_url: https://arxiv.org/pdf/2610.22325
published: '2026-10-15'
collected: '2026-10-18'
category: Other
direction: 4D人体运动重建 · 稠密对应
tags:
- 4D_Human_Reconstruction
- Dense_Correspondence
- Monocular_RGB
- Feed_Forward_Model
- Human_Point_Map
one_liner: 首个无需人体模板的前馈模型，仅用单目RGB序列实现含服装毛发的人体像素级4D稠密对应
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 6
source: arxiv-cs.CV
depth: abstract
---

## 动机
现有4D人体运动重建方案依赖预定义人体模板、相机位姿估计，难以适配服装/毛发形变、遮挡场景下的跨帧表面点匹配需求。
## 方法关键点
1. 无模板前馈框架Dense4D输入带已知裁剪变换的中心化人体RGB裁剪框，联合输出每帧Human Point Map（HPM）与深度；
2. HPM将每个属于人体的像素映射到公共参考时刻的表面点3D坐标，支持amodal对应：参考帧遮挡点可通过其他帧观测定位；
3. 跨帧匹配HPM坐标即可建立对应关系，无需预测相机位姿或大场景位移，结合单帧深度即可升维得到3D跟踪轨迹。
## 关键结果
实测跟踪精度、与扫描曲面的贴合度均显著优于基线，可在关节活动、服装形变场景下生成一致的稠密对应结果。
