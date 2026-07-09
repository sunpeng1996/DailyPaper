---
title: 'ProxyPose: 6-DoF Pose Tracking via Video-to-Video Translation'
title_zh: ProxyPose：基于视频到视频翻译的6自由度位姿跟踪
authors:
- Ruihang Zhang
- Felix Taubner
- Pooja Ravi
- Kiriakos N. Kutulakos
- David B. Lindell
affiliations:
- University of Toronto
- Vector Institute
arxiv_id: '2607.06555'
url: https://arxiv.org/abs/2607.06555
pdf_url: https://arxiv.org/pdf/2607.06555
published: '2026-07-07'
collected: '2026-07-09'
category: Other
direction: 计算机视觉 · 6自由度位姿跟踪
tags:
- PoseTracking
- VideoDiffusion
- VideoTranslation
- 6DoF
- ComputerVision
one_liner: 将6-DoF位姿跟踪转化为视频到视频翻译任务，仅需视频加首帧标记像素即实现SOTA跟踪精度
practical_value: '- 可借鉴「复杂任务转化为生成任务+传统工具求解」的范式：将难以直接建模的业务目标，先通过生成模型输出已知结构的中间代理结果，再用成熟规则/工具链解最终任务，降低端到端建模的标注成本

  - 针对难样本泛化问题，可考虑用预训练生成模型吸收复杂场景适配逻辑，仅需少量合成/标注数据微调即可适配下游任务，降低对真实业务标注的依赖'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
单目视频6-DoF位姿跟踪是计算机视觉领域长期难题，现有方法依赖视频外的额外输入（如3D模型、深度图、物体掩码等），在无纹理、透明、反光、可形变表面上表现不佳，且通常需要物体身份、全局刚性等强假设。
### 方法关键点
将位姿跟踪重定义为视频到视频翻译任务：仅输入原始视频+首帧单个标记像素，通过合成数据微调的视频扩散模型生成代理视频——用几何、外观已知的彩色多面体同步模拟标记像素对应表面区域的局部刚体运动，再直接调用现成的经典位姿求解器从代理视频解算6-DoF轨迹，无需额外输入或物体相关假设。
### 关键结果
无需额外输入即可达到6-DoF位姿跟踪SOTA精度，仅需合成数据完成视频模型微调，可拓展至人脸跟踪、相机位姿估计、野外复杂场景等现有方法无法覆盖的场景。
