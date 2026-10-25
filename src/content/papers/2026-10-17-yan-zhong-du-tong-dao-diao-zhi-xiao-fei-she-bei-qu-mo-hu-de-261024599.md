---
title: 'Severity-Channel Conditioning: An Injection-Level Study for Consumer-Device
  Deblurring'
title_zh: 严重度通道调制：消费设备去模糊的信息注入层级研究
authors:
- Abdullah Al Shafi
- Kazi Saeed Alam
- Sumaiya Rahim Suma
- Sk. Imran Hossain
arxiv_id: '2610.24599'
url: https://arxiv.org/abs/2610.24599
pdf_url: https://arxiv.org/pdf/2610.24599
published: '2026-10-17'
collected: '2026-10-25'
category: Other
direction: 消费设备图像去模糊 · 条件信息注入优化
tags:
- Image Deblurring
- Diffusion Model
- Domain Adaptation
- Privileged Information
- Consumer Imaging
one_liner: 对比消费设备去模糊任务中多种严重度信息注入方式的效果，验证输入级拼接方案的性能增益
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有运动去模糊模型多基于专业相机数据训练，迁移到智能手机等消费设备时精度损失严重，缺少适配性验证方案。
### 方法关键点
以域适配后的latent diffusion为统一基线，在相同微调预算下对比4类信息注入方案的效果：输入侧拼接严重度图、拍摄元数据全局特征调制、严重度图空间特征调制、分层对比输出目标+无约束谱损失控制，主实验为推理阶段注入真值衍生信息的oracle诊断。
### 关键结果
- 输入拼接方案将整体PSNR从基线31.23dB提升至31.30dB，其余方案均未超过基线
- 增益在87.2%的测试图像、14/15的留出源视频上为正，且在Transformer backbone上可复现
- 推理阶段置零严重度通道可保留大部分PSNR增益，但SSIM低于基线
